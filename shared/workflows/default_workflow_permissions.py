from oarepo_workflows import (
    WorkflowRequestPolicy,
    IfInState,
    WorkflowRequest,
    WorkflowTransitions,
    AutoApprove,
    WorkflowRequestEscalation,
)
from oarepo_runtime.services.permissions import UserWithRole, RecordOwners
from oarepo_communities.services.permissions.generators import CommunityRole, CommunityMembers
from invenio_communities.generators import CommunityMembers, IfRestricted
from oarepo_workflows.services.permissions import DefaultWorkflowPermissions
from invenio_records_permissions.generators import AnyUser

class DefaultWorkflowPermissions(DefaultWorkflowPermissions):
    can_create = [
        UserWithRole("administrator"),
        CommunityRole("editor"),
    ]
 
    can_read = [
        RecordOwners(),
        # curator can see the record in any state
        CommunityRole("curator"),
        # administrator can see everything
        UserWithRole("administrator"),
        # if the record is published and restricted, only members of the community can see it,
        # otherwise, any user can see it
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
 
    can_update = [
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                CommunityRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
        # if not draft, can not be directly updated by any means, must use request
    ]
 
    can_delete = [
        # draft can be deleted, published record must be deleted via request
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                CommunityRole("curator"),
                UserWithRole("administrator"),
            ],
        ),
    ]

