from invenio_records_permissions import BasePermissionPolicy
from oarepo_communities.services.permissions.generators import CommunityRole
from oarepo_runtime.services.generators import RecordOwners
from oarepo_runtime.services.permissions import UserWithRole


class ExperimentsWorkflowPermissions(BasePermissionPolicy):
    can_curator_action = [
        RecordOwners(),
        CommunityRole("curator"),
        UserWithRole("administrator"),
    ]
    can_record_action = [RecordOwners(), CommunityRole("editor")]
