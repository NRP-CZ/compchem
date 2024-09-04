from experiments.files.api import ExperimentsFile, ExperimentsFileDraft
from experiments.files.requests.resolvers import ExperimentsFileDraftResolver
from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.records.requests.resolvers import (
    ExperimentsDraftResolver,
    ExperimentsResolver,
)
from experiments.resources.files.config import (
    ExperimentsFileDraftResourceConfig,
    ExperimentsFileResourceConfig,
)
from experiments.resources.files.resource import (
    ExperimentsFileDraftResource,
    ExperimentsFileResource,
)
from experiments.resources.records.config import ExperimentsResourceConfig
from experiments.resources.records.resource import ExperimentsResource
from experiments.services.files.config import (
    ExperimentsFileDraftServiceConfig,
    ExperimentsFileServiceConfig,
)
from experiments.services.files.service import (
    ExperimentsFileDraftService,
    ExperimentsFileService,
)
from experiments.services.records.config import ExperimentsServiceConfig
from experiments.services.records.service import ExperimentsService
from oarepo_requests.resolvers.ui import (
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService

EXPERIMENTS_RECORD_RESOURCE_CONFIG = ExperimentsResourceConfig


EXPERIMENTS_RECORD_RESOURCE_CLASS = ExperimentsResource


EXPERIMENTS_RECORD_SERVICE_CONFIG = ExperimentsServiceConfig


EXPERIMENTS_RECORD_SERVICE_CLASS = ExperimentsService


OAREPO_PRIMARY_RECORD_SERVICE = {
    ExperimentsRecord: "experiments",
    ExperimentsDraft: "experiments",
    ExperimentsFile: "experiments_file",
    ExperimentsFileDraft: "experiments_file_draft",
}


EXPERIMENTS_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


EXPERIMENTS_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


EXPERIMENTS_ENTITY_RESOLVERS = [
    ExperimentsResolver(
        record_cls=ExperimentsRecord, service_id="experiments", type_key="experiments"
    ),
    ExperimentsDraftResolver(
        record_cls=ExperimentsDraft,
        service_id="experiments",
        type_key="experiments_draft",
    ),
    ExperimentsFileDraftResolver(
        record_cls=ExperimentsFileDraft,
        service_id="experiments_file_draft",
        type_key="experiments_file_draft",
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "experiments": RecordEntityReferenceUIResolver("experiments"),
    "experiments_draft": RecordEntityDraftReferenceUIResolver("experiments_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = []


EXPERIMENTS_FILES_RESOURCE_CONFIG = ExperimentsFileResourceConfig


EXPERIMENTS_FILES_RESOURCE_CLASS = ExperimentsFileResource


EXPERIMENTS_FILES_SERVICE_CONFIG = ExperimentsFileServiceConfig


EXPERIMENTS_FILES_SERVICE_CLASS = ExperimentsFileService


EXPERIMENTS_DRAFT_FILES_RESOURCE_CONFIG = ExperimentsFileDraftResourceConfig


EXPERIMENTS_DRAFT_FILES_RESOURCE_CLASS = ExperimentsFileDraftResource


EXPERIMENTS_DRAFT_FILES_SERVICE_CONFIG = ExperimentsFileDraftServiceConfig


EXPERIMENTS_DRAFT_FILES_SERVICE_CLASS = ExperimentsFileDraftService
