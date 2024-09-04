from experiments.records.models import ExperimentsDraftMetadata, ExperimentsMetadata
from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin


class ExperimentsFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for ExperimentsFile metadata."""

    __tablename__ = "experiments_file_metadata"
    __record_model_cls__ = ExperimentsMetadata


class ExperimentsFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for ExperimentsFileDraft metadata."""

    __tablename__ = "experiments_file_draft_metadata"
    __record_model_cls__ = ExperimentsDraftMetadata
