## ⚠️ I had to temporairly switch from oarepo_communities to invenio_communities

from oarepo_workflows import (
    WorkflowRequestPolicy,
    IfInState,
    WorkflowRequest,
    WorkflowTransitions,
    AutoApprove,
    WorkflowRequestEscalation,
)
from oarepo_runtime.services.permissions import UserWithRole, RecordOwners
## from oarepo_communities.services.permissions.generators import CommunityRole, CommunityMembers
from invenio_communities.generators import CommunityMembers, CommunityCurators, IfRestricted
from oarepo_workflows import DefaultWorkflowPermissions
from invenio_records_permissions.generators import AnyUser

class DefaultWorkflowPermissions(DefaultWorkflowPermissions):
    can_create = [
        ## CommunityRole("editor"),
        CommunityMembers(),
    ]
 
    can_read = [
        RecordOwners(),
        # curator can see the record in any state
        ## CommunityRole("curator"),
        CommunityCurators(),
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
 
        ## IfInState("retracting", then_=[RecordOwners(), CommunityRole("curator")]),
        IfInState("retracting", then_=[RecordOwners(), CommunityCurators()]),
    ]
 
    can_update = [
        IfInState(
            "draft",
            then_=[
                RecordOwners(),
                ## CommunityRole("curator"),
                CommunityCurators(),
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
                ## ommunityRole("curator"),
                CommunityCurators(),
                UserWithRole("administrator"),
            ],
        ),
    ]

