from flask import jsonify, request
from flask_resources import response_handler, route
from invenio_records_resources.resources import RecordResource
import requests


class ExperimentsWorkflowResource(RecordResource):
    """Experiments workflow resource."""

    def create_url_rules(self):
        """Create the URL rules for the workflow resource."""
        routes = self.config.routes
        return [
            route("GET", routes["list"], self.get),
            route("POST", routes["available"], self.post_available),
            route("POST", routes["create"], self.post_create),
        ]

    @response_handler()
    def get(self):
        """Handle GET request to return hello world."""
        return jsonify({"message": "hello world"}), 200

    @response_handler()
    def post_available(self):
        """Proxy POST request to fetch available workflows."""
        try:
            data = request.get_json()

            go_api_url = "http://localhost:8062/api/v1/workflows/available"
            response = requests.post(
                go_api_url,
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            return jsonify(response.json()), response.status_code

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to connect to workflow service: {str(e)}"}), 502
        except Exception as e:
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    @response_handler()
    def post_create(self):
        """Proxy POST request to create workflow."""
        try:
            data = request.get_json()

            go_api_url = "http://localhost:8062/api/v1/workflows"
            response = requests.post(
                go_api_url,
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=30
            )

            return jsonify(response.json()), response.status_code

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to connect to workflow service: {str(e)}"}), 502
        except Exception as e:
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500
