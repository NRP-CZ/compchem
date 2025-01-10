from invenio_communities.records.records.systemfields import CommunitiesField
from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_communities.records.systemfields.communities import (
    OARepoCommunitiesFieldContext,
)
from oarepo_runtime.records.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.records.systemfields.owner import OwnersField
from oarepo_runtime.records.systemfields.record_status import RecordStatusSystemField
from oarepo_workflows.records.systemfields.state import (
    RecordStateField,
    RecordStateTimestampField,
)
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from experiments.files.api import ExperimentsFile, ExperimentsFileDraft
from experiments.records.dumpers.dumper import ExperimentsDraftDumper, ExperimentsDumper
from experiments.records.models import (
    ExperimentsCommunitiesMetadata,
    ExperimentsDraftMetadata,
    ExperimentsMetadata,
    ExperimentsParentMetadata,
    ExperimentsParentState,
)


class ExperimentsParentRecord(ParentRecord):
    model_cls = ExperimentsParentMetadata

    workflow = WorkflowField()

    communities = CommunitiesField(
        ExperimentsCommunitiesMetadata, context_cls=OARepoCommunitiesFieldContext
    )

    owners = OwnersField()


class ExperimentsIdProvider(DraftRecordIdProviderV2):
    pid_type = "xprnts"


class ExperimentsRecord(InvenioRecord):

    model_cls = ExperimentsMetadata

    schema = ConstantField("$schema", "local://experiments-1.0.0.json")

    index = IndexField(
        "experiments-experiments-1.0.0",
    )

    pid = PIDField(
        provider=ExperimentsIdProvider, context_cls=PIDFieldContext, create=True
    )

    dumper = ExperimentsDumper()

    state = RecordStateField(initial="published")

    state_timestamp = RecordStateTimestampField()

    versions_model_cls = ExperimentsParentState

    parent_record_cls = ExperimentsParentRecord
    record_status = RecordStatusSystemField()
    has_draft = HasDraftCheckField(
        draft_cls=lambda: ExperimentsDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
    )

    files = FilesField(
        file_cls=ExperimentsFile, store=False, create=False, delete=False
    )

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class ExperimentsDraft(InvenioDraft):

    model_cls = ExperimentsDraftMetadata

    schema = ConstantField("$schema", "local://experiments-1.0.0.json")

    index = IndexField(
        "experiments-experiments_draft-1.0.0", search_alias="experiments"
    )

    pid = PIDField(
        provider=ExperimentsIdProvider,
        context_cls=PIDFieldContext,
        create=True,
        delete=False,
    )

    dumper = ExperimentsDraftDumper()

    state = RecordStateField()

    state_timestamp = RecordStateTimestampField()

    versions_model_cls = ExperimentsParentState

    parent_record_cls = ExperimentsParentRecord
    record_status = RecordStatusSystemField()

    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=ExperimentsFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


ExperimentsFile.record_cls = ExperimentsRecord

ExperimentsFileDraft.record_cls = ExperimentsDraft
