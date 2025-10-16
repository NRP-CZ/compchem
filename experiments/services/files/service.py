from invenio_records_resources.services import FileService
from oarepo_requests.services.results import PermissionDeniedError

from experiments.records.models import ExperimentsWorkflowContext


class ExperimentsFileService(FileService):
    """ExperimentsFile service."""


class ExperimentsFileDraftService(FileService):
    """ExperimentsFileDraft service."""

    def authenticate_request(self, record_id: str, secret_key: str) -> bool:
        """Verify secret key for the given record."""
        try:
            context = ExperimentsWorkflowContext.query.filter_by(
                experiment_id=record_id, secret_key=secret_key
            ).first()

            if context is not None:
                return True
            else:
                return False
        except Exception:
            return False

    def read_file(self, identity, id_, file_key, secret_key, **kwargs):
        """Generate S3 signed URLs for reading files."""

        if not self.authenticate_request(id_, secret_key):
            raise PermissionDeniedError("workflow_read_file")

        return self.get_file_content(
            identity=identity, id_=id_, file_key=file_key, kwargs=kwargs
        )

    def write_file(self, identity, id_, file_key, stream, secret_key, **kwargs):
        if not self.authenticate_request(id_, secret_key):
            raise PermissionDeniedError("workflow_write_file")

        self.init_files(identity=identity, id_=id_, data=[{"key": file_key}])

        self.set_file_content(
            identity=identity,
            id_=id_,
            file_key=file_key,
            stream=stream,
            content_length=kwargs["content_length"],
        )

        return self.commit_file(
            identity=identity,
            id_=id_,
            file_key=file_key,
        )
