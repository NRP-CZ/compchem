import importlib_metadata
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig

from experiments.resources.records.ui import ExperimentsUIJSONSerializer


class ExperimentsResourceConfig(RecordResourceConfig):
    """ExperimentsRecord resource config."""

    blueprint_name = "experiments"
    url_prefix = "/experiments/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.experiments.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ExperimentsUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
