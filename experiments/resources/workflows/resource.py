import sys

from flask import current_app, g, jsonify, request
from flask_resources import Resource, route


class ExperimentsWorkflowResource(Resource):
    """Experiments workflow resource."""

    @property
    def service(self):
        """Get the workflow service."""
        return current_app.extensions["experiments-workflows"].service_workflows

    def create_url_rules(self):
        """Create the URL rules for the workflow resource."""
        routes = self.config.routes
        return [
            route("POST", routes["available"], self.post_available),
            route("POST", routes["create"], self.post_create),
            route("POST", routes["create_all"], self.post_create_all),
            route("GET", routes["list"], self.get_list_workflows),
            route("GET", routes["detail"], self.get_workflow_detail),
            route("GET", routes["logs"], self.get_workflow_logs),
            route("DELETE", routes["delete_context"], self.delete_workflow_context),
        ]

    def post_available(self):
        """Proxy POST request to fetch available workflows."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        data = request.get_json()
        record_id = request.view_args.get("record_id")

        result, status_code = self.service.get_available_workflows(
            identity=g.identity, data=data, id_=record_id
        )

        print("status: " + str(status_code), file=sys.stderr)
        return jsonify(result), status_code

    def post_create(self):
        """Proxy POST request to create workflow."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        record_id = request.view_args.get("record_id")
        data = request.get_json()

        result, status_code = self.service.create_workflow(
            identity=g.identity, record_id=record_id, data=data
        )
        return jsonify(result), status_code

    def post_create_all(self):
        """Proxy POST request to create all workflows."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        record_id = request.view_args.get("record_id")
        data = request.get_json()

        result, status_code = self.service.create_all_workflows(
            identity=g.identity, record_id=record_id, data=data
        )
        return jsonify(result), status_code

    def get_list_workflows(self):
        """Proxy GET request to list record workflows."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        record_id = request.view_args.get("record_id")
        skip = request.args.get("skip", default=0, type=int)
        limit = request.args.get("limit", default=5, type=int)
        status_filter = request.args.get("status", default="", type=str)

        result, status_code = self.service.list_workflows(
            identity=g.identity,
            record_id=record_id,
            skip=skip,
            limit=limit,
            status_filter=status_filter if status_filter else None,
        )
        return jsonify(result), status_code

    def get_workflow_detail(self):
        """Proxy GET request to fetch workflow detail."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        workflow_name = request.view_args.get("workflow_name")
        record_id = request.view_args.get("record_id")
        result, status_code = self.service.get_workflow_detail(
            identity=g.identity, record_id=record_id, workflow_name=workflow_name
        )
        return jsonify(result), status_code

    def get_workflow_logs(self):
        """Proxy GET request to fetch workflow logs from Argo."""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        workflow_name = request.view_args.get("workflow_name")
        record_id = request.view_args.get("record_id")
        result, status_code = self.service.get_workflow_logs(
            identity=g.identity, record_id=record_id, workflow_name=workflow_name
        )
        return jsonify(result), status_code

    def delete_workflow_context(self):
        """Remove context of workflow"""
        if request.view_args is None:
            return jsonify({"error": "request view args must be defined"}), 400

        workflow_name = request.view_args.get("workflow_name")
        secret_key = request.args.get("secret_key")
        result, status_code = self.service.remove_workflow_context(
            identity=g.identity, workflow_name=workflow_name, secret_key=secret_key
        )
        return jsonify(result), status_code
