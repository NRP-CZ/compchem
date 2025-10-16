import json
from typing import Any, Dict

import requests
from flask import current_app
from invenio_db import db
from invenio_records_resources.services import Service
from sqlalchemy.exc import NoResultFound

from experiments.records.models import ExperimentsWorkflowContext


class ExperimentsWorkflowService(Service):
    """Stateless service for workflow operations."""

    @property
    def fileprocessor_url(self):
        """Get the fileprocessor URL from config."""
        return current_app.config.get("FILEPROCESSOR_URL")

    @property
    def argo_url(self):
        """Get the Argo workflows URL from config."""
        return current_app.config.get("ARGO_WORKFLOWS_URL")

    @property
    def record_cls(self):
        """Get the record class."""
        return self.config.record_cls

    @property
    def draft_cls(self):
        """Get the draft record class."""
        return self.config.draft_cls

    def _check_workflows_enabled(self):
        """Check if workflows are enabled by verifying required URLs are configured."""
        if not self.fileprocessor_url or not self.argo_url:
            return (
                False,
                {"error": "Workflows are not enabled - missing configuration"},
                503,
            )
        return True, None, None

    def _resolve_record(self, id_):
        try:
            record = self.record_cls.pid.resolve(id_, registered_only=False)
        except NoResultFound:
            record = self.draft_cls.pid.resolve(id_, registered_only=False)

        return record

    def _register_workflow_context(self, experiment_id, workflow_name, secret_key):
        """Register workflow context in the database."""
        new_context = ExperimentsWorkflowContext(
            workflow_name=workflow_name,
            secret_key=secret_key,
            experiment_id=experiment_id,
        )
        db.session.add(new_context)
        db.session.commit()

    def _do_external_call(
        self, method: str, url: str, json_data=None, params=None, expected_status=200
    ) -> tuple[Dict[str, Any], int]:
        """Perform a standardized external HTTP call."""
        try:
            response = requests.request(
                method=method,
                url=url,
                json=json_data,
                params=params,
                headers={"Content-Type": "application/json"},
                timeout=30,
                verify=False,
            )

            if response.status_code != expected_status:
                return {
                    "error": f"Unexpected status code received: {response.status_code}, expected: {expected_status}",
                    "status": 500,
                }, 500

            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            return {
                "error": f"Request to external service failed: {str(e)}",
            }, 502
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}, 500

    def get_available_workflows(self, record_id, identity, data):
        """Get available workflows."""

        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "curator_action", record=record)

        api_url = f"{self.fileprocessor_url}/v1/workflows/available"

        return self._do_external_call(
            "POST", api_url, json_data=data, expected_status=201
        )

    def create_workflow(self, identity, record_id, data):
        """Create a workflow for a specific record."""
        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "curator_action", record=record)

        go_api_url = f"{self.fileprocessor_url}/v1/workflows/{record_id}"

        response_data, status = self._do_external_call(
            "POST", go_api_url, json_data=data, expected_status=201
        )

        if (
            status == 201
            and "workflowName" in response_data
            and "secretKey" in response_data
        ):
            try:
                self._register_workflow_context(
                    record_id,
                    response_data["workflowName"],
                    response_data["secretKey"],
                )
            except Exception as e:
                db.session.rollback()
                return {
                    "error": f"Workflow created but failed to register context: {str(e)}",
                    "workflow_data": response_data,
                }, 500

        return response_data, status

    def create_all_workflows(self, identity, record_id, data):
        """Create all workflows for a specific record."""
        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "record_action", record=record)

        go_api_url = f"{self.fileprocessor_url}/v1/workflows/{record_id}/all"

        response_data, status = self._do_external_call(
            "POST", go_api_url, json_data=data, expected_status=201
        )

        if status == 201:
            try:
                for context in response_data["workflowContexts"]:
                    self._register_workflow_context(
                        record_id, context["workflowName"], context["secretKey"]
                    )
            except Exception as e:
                db.session.rollback()
                return {
                    "error": f"Workflows created but failed to register contexts: {str(e)}",
                    "workflow_data": response_data,
                }, 500

        return response_data, status

    def list_workflows(self, identity, record_id, skip=0, limit=5, status_filter=None):
        """List workflows for a specific record."""
        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "record_action", record=record)

        params: Dict[str, Any] = {"skip": skip, "limit": limit}
        if status_filter:
            params["status"] = status_filter

        go_api_url = f"{self.fileprocessor_url}/v1/workflows/{record_id}/list"

        return self._do_external_call("GET", go_api_url, params=params)

    def get_workflow_detail(self, identity, record_id, workflow_name):
        """Get workflow detail."""
        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "curator_action", record=record)

        go_api_url = f"{self.fileprocessor_url}/v1/workflows/{workflow_name}/detail"

        return self._do_external_call("GET", go_api_url)

    def get_workflow_logs(self, identity, record_id, workflow_name):
        """Get workflow logs from Argo."""
        enabled, error_response, status_code = self._check_workflows_enabled()
        if not enabled:
            return error_response, status_code

        record = self._resolve_record(record_id)

        self.require_permission(identity, "curator_action", record=record)

        try:
            argo_url = f"{self.argo_url}/api/v1/workflows/argo/{workflow_name}/log"
            params = {
                "logOptions.container": "main",
                "grep": "",
                "logOptions.follow": "false",
            }

            response = requests.get(
                argo_url,
                params=params,
                stream=True,
                timeout=30,
                verify=False,  # todo: certs?
            )

            if response.status_code != 200:
                return {
                    "error": f"Argo server returned status {response.status_code}"
                }, response.status_code

            logs = []

            for line in response.iter_lines(decode_unicode=True):
                if line and line.strip():
                    log_entry = json.loads(line.strip())
                    logs.append(log_entry)

            return {
                "logs": logs,
                "total_entries": len(logs),
                "workflow_name": workflow_name,
            }, 200

        except requests.exceptions.RequestException as e:
            return {"error": f"Failed to connect to Argo server: {str(e)}"}, 502
        except Exception as e:
            return {"error": f"Internal server error: {str(e)}"}, 500

    def remove_workflow_context(self, identity, workflow_name, secret_key):
        """Remove workflow context from the database."""
        try:
            if not workflow_name or not secret_key:
                return {"error": "workflow_name and secret_key are required"}, 400

            context = ExperimentsWorkflowContext.query.filter_by(
                workflow_name=workflow_name, secret_key=secret_key
            ).first()

            if not context:
                return {
                    "error": "Workflow context not found or invalid secret key"
                }, 404

            db.session.delete(context)
            db.session.commit()

            return {"message": "Workflow context removed successfully"}, 200

        except Exception as e:
            db.session.rollback()
            return {"error": f"Failed to remove workflow context: {str(e)}"}, 500
