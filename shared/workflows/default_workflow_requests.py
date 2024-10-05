from datetime import timedelta
from oarepo_workflows import (
    WorkflowRequestPolicy,
    IfInState,
    WorkflowRequest,
    WorkflowTransitions,
    AutoApprove,
    WorkflowRequestEscalation,
)
from oarepo_runtime.services.permissions import UserWithRole, RecordOwners
from oarepo_requests.services.permissions.generators import IfRequestedBy
## from oarepo_communities.services.permissions.generators import CommunityRole
from invenio_communities.generators import CommunityCurators
 
 
class DefaultWorkflowRequests(WorkflowRequestPolicy):
    """Specific requests here"""
    delete_request = WorkflowRequest(
        requesters = [
            ## IfInState("published", [RecordOwners(), CommunityRole("curator")]),
            IfInState("published", [RecordOwners(), CommunityCurators()]),
            
        ],
        recipients = [
            IfRequestedBy(
                ## CommunityRole("curator"),
                CommunityCurators(),
                then_=[AutoApprove()],
                ## else_=[CommunityRole("curator")],
                else_=[CommunityCurators()],
            )
        ],
        transitions = WorkflowTransitions(
            submitted = 'deleting',
            accepted = 'deleted',
            declined = 'draft'
        ),
        escalations = [
            WorkflowRequestEscalation(
                after=timedelta(days=14),
                recipients=[UserWithRole("administrator")]
            )
        ]
    )
