from oarepo_requests.types.publish_draft import PublishDraftRequestType
from oarepo_runtime.i18n import lazy_gettext as _


class PublishDraftRequestType(PublishDraftRequestType):

    type_id = "experiments_publish_draft"
    name = _("Publish draft")

    available_actions = {
        **PublishDraftRequestType.available_actions,
    }

    allowed_topic_ref_types = [
        "experiments_draft"
    ]  # On the Request record object, the topic is referenced by pid. This pid is
    # extracted by Resolver subclassed from RecordResolver, which has hardcoded
    # {"record": {pid}} as reference value. This reference is then by
    # setattr set on the Request record topic ReferencedEntityField, and the set
    # operation checks, whether this key is in allowed_topic_ref_types

    allowed_receiver_ref_types = ["user", "group"]

    # Invenio fails on this method as it is not marked as classmethod in invenio sources.
    # It will be removed in future versions, till the removal (or fix) we need to provide
    # our own implementation here.
    @classmethod
    def _update_link_config(cls, **context_values):
        """Method for updating the context values when generating links.

        WARNING: this method potentially mixes layers and might be a footgun;
        it will likely be removed in a future release!

        This method takes the already determined context values for the link as
        keyword arguments and should return values that will be used to update the
        original context values.
        """
        # FIXME/TODO this should be reworked into a service feature
        return {}
