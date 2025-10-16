from invenio_records_resources.services import ServiceConfig
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_runtime.services.components import OwnersComponent
from oarepo_runtime.services.config import PermissionsPresetsConfigMixin

from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.services.worfklows.permissions import ExperimentsWorkflowPermissions


class ExperimentsWorkflowServiceConfig(PermissionsPresetsConfigMixin, ServiceConfig):
    """Configuration for the experiments workflow service."""

    service_id = "experiments_workflows"

    PERMISSIONS_PRESETS = []

    base_permission_policy_cls = ExperimentsWorkflowPermissions

    components = [
        CommunityInclusionComponent,
        OwnersComponent,
    ]

    record_cls = ExperimentsRecord

    draft_cls = ExperimentsDraft
