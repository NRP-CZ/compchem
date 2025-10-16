from invenio_communities.generators import CommunityMembers, IfRestricted
from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import AuthenticatedUser
from invenio_requests.services.permissions import AnyUser
from oarepo_communities.services.permissions.generators import CommunityRole
from oarepo_runtime.services.components import RecordOwners
from oarepo_runtime.services.permissions import UserWithRole
from oarepo_workflows import IfInState

# from invenio_records_permissions.generators import SystemProcess, AnyUser


class ExperimentsPermissionPolicy(RecordPermissionPolicy):
    """experiments.records.api.ExperimentsRecord permissions.
    Values in this class will be merged with permission presets.
    """

    can_search = [AuthenticatedUser()]
    can_read = [
        RecordOwners(),
        CommunityRole("curator"),
        UserWithRole("administrator"),
        IfInState(
            "published",
            then_=[
                IfRestricted(
                    "visibility",
                    then_=[CommunityMembers()],
                    else_=[AnyUser()],
                )
            ],
        ),
        IfInState("retracting", then_=[RecordOwners(), CommunityRole("curator")]),
    ]
    can_create = [AuthenticatedUser()]
    can_update = [
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                CommunityRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
    ]
    can_delete = [
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                CommunityRole("curator"),
                UserWithRole("administrator"),
            ],
        )
    ]
    can_manage = [AuthenticatedUser()]
    can_read_files = [AuthenticatedUser()]
    can_update_files = [AuthenticatedUser()]

    # Additional permissions that might be needed for full functionality
    can_publish = [AuthenticatedUser()]
    can_edit = []
    can_review = [AuthenticatedUser()]
    can_read_draft = [AuthenticatedUser()]
    can_update_draft = [AuthenticatedUser()]
    can_delete_draft = [AuthenticatedUser()]
    can_new_version = [AuthenticatedUser()]
    can_search_versions = [AuthenticatedUser()]
