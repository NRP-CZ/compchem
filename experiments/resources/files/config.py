import importlib_metadata
from experiments.resources.files.ui import (
    ExperimentsFileDraftUIJSONSerializer,
    ExperimentsFileUIJSONSerializer,
)
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig


class ExperimentsFileResourceConfig(FileResourceConfig):
    """ExperimentsFile resource config."""

    blueprint_name = "experiments_file"
    url_prefix = "/experiments/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.experiments.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ExperimentsFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class ExperimentsFileDraftResourceConfig(FileResourceConfig):
    """ExperimentsFileDraft resource config."""

    blueprint_name = "experiments_file_draft"
    url_prefix = "/experiments/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.experiments.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ExperimentsFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
