from flask import current_app, g
from flask_resources import (
    JSONDeserializer,
    RequestBodyParser,
    request_body_parser,
    request_parser,
    resource_requestctx,
    response_handler,
    route,
)
from flask_resources.parsers.base import ma
from invenio_rdm_records.records.stats.api import current_stats
from invenio_records_resources.resources.files.parser import RequestStreamParser
from invenio_records_resources.resources.files.resource import FileResource
from oarepo_ui.resources.file_resource import S3RedirectFileResource

request_view_args = request_parser(
    {"pid_value": ma.fields.Str(required=True), "key": ma.fields.Str()},
    location="view_args",
)

request_data = request_body_parser(
    parsers={"application/json": RequestBodyParser(JSONDeserializer())},
    default_content_type="application/json",
)

request_search_args = request_parser(
    {"secret_key": ma.fields.Str(required=True)},
    location="args",
)

request_stream = request_body_parser(
    parsers={"application/octet-stream": RequestStreamParser()},
    default_content_type="application/octet-stream",
)


class ExperimentsFileResource(S3RedirectFileResource):
    """ExperimentsFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class ExperimentsFileDraftResource(FileResource):
    """ExperimentsFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules

    def create_url_rules(self):
        """Create the URL rules for the workflow files resource."""
        routes = self.config.routes

        url_rules = super().create_url_rules()
        url_rules += [
            route(
                "GET",
                routes["item-content-workflow"],
                self.post_workflow_read_file,
            ),
            route(
                "POST",
                routes["item-commit-workflow"],
                self.post_workflow_commit_file,
            ),
        ]

        return url_rules

    @request_search_args
    @request_data
    @request_view_args
    def post_workflow_read_file(self):
        """Read file content."""
        item = self.service.read_file(
            g.identity,
            resource_requestctx.view_args["pid_value"],
            resource_requestctx.view_args["key"],
            resource_requestctx.args["secret_key"],
        )

        # emit file download stats event
        obj = item._file.object_version
        emitter = current_stats.get_event_emitter("file-download")
        if obj is not None and emitter is not None:
            emitter(current_app, record=item._record, obj=obj, via_api=True)

        return item.send_file()

    @request_view_args
    @request_search_args
    @request_stream
    @response_handler()
    def post_workflow_commit_file(self):
        """Commit a file."""
        item = self.service.write_file(
            g.identity,
            resource_requestctx.view_args["pid_value"],
            resource_requestctx.view_args["key"],
            resource_requestctx.data["request_stream"],
            resource_requestctx.args["secret_key"],
            content_length=resource_requestctx.data["request_content_length"],
        )
        return item.to_dict(), 200
