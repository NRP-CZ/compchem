from invenio_records_resources.resources import RecordResourceConfig


class ExperimentsWorkflowResourceConfig(RecordResourceConfig):
    """Experiments workflow resource configuration."""

    blueprint_name = "experiments_workflows"
    url_prefix = "/workflows"

    routes = {
        "available": "/<record_id>/available",
        "create": "/<record_id>",
        "create_all": "/<record_id>/all",
        "list": "/<record_id>/list",
        "detail": "/<record_id>/<workflow_name>/detail",
        "logs": "/<record_id>/<workflow_name>/logs",
        "delete_context": "/<workflow_name>/context",
    }
