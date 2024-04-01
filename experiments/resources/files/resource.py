from invenio_records_resources.resources.files.resource import FileResource
from oarepo_ui.resources.file_resource import S3RedirectFileResource


class ExperimentsFileResource(S3RedirectFileResource):
    """ExperimentsFile resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules


class ExperimentsFileDraftResource(FileResource):
    """ExperimentsFileDraft resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
