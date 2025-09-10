from invenio_records_resources.resources import RecordResourceConfig 


class ExperimentsWorkflowResourceConfig(RecordResourceConfig):
    """Experiments workflow resource configuration."""

    blueprint_name = "experiments_workflows"
    url_prefix = "/workflows"

    routes = {
        "list": "/",
        "available": "/available",
        "create": "/",
    }
