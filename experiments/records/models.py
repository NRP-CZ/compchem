from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from oarepo_workflows.records.models import RecordWorkflowParentModelMixin
from sqlalchemy_utils import UUIDType


class ExperimentsParentMetadata(
    RecordWorkflowParentModelMixin, db.Model, RecordMetadataBase
):

    __tablename__ = "experiments_parent_record_metadata"


class ExperimentsMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for ExperimentsRecord metadata."""

    __tablename__ = "experiments_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = ExperimentsParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class ExperimentsDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for ExperimentsDraft metadata."""

    __tablename__ = "experiments_draft_metadata"

    __parent_record_model__ = ExperimentsParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class ExperimentsParentState(db.Model, ParentRecordStateMixin):
    table_name = "experiments_parent_state_metadata"

    __parent_record_model__ = ExperimentsParentMetadata
    __record_model__ = ExperimentsMetadata
    __draft_model__ = ExperimentsDraftMetadata
