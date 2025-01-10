from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    LinksTemplate,
    RecordLink,
    pagination_links,
)
from oarepo_communities.services.components.default_workflow import (
    CommunityDefaultWorkflowComponent,
)
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_communities.services.links import CommunitiesLinks
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    OwnersComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_draft,
    has_file_permission,
    has_permission,
    has_published_record,
    is_published_record,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.records import pagination_links_html
from oarepo_workflows.services.components.workflow import WorkflowComponent

from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.services.records.permissions import ExperimentsPermissionPolicy
from experiments.services.records.results import (
    ExperimentsRecordItem,
    ExperimentsRecordList,
)
from experiments.services.records.schema import ExperimentsSchema
from experiments.services.records.search import ExperimentsSearchOptions


class ExperimentsServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """ExperimentsRecord service config."""

    result_item_cls = ExperimentsRecordItem

    result_list_cls = ExperimentsRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/experiments/"

    base_permission_policy_cls = ExperimentsPermissionPolicy

    schema = ExperimentsSchema

    search = ExperimentsSearchOptions

    record_cls = ExperimentsRecord

    service_id = "experiments"

    search_item_links_template = LinksTemplate
    draft_cls = ExperimentsDraft
    search_drafts = ExperimentsSearchOptions

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [
            CommunityDefaultWorkflowComponent,
            CommunityInclusionComponent,
            OwnersComponent,
            DraftFilesComponent,
            FilesComponent,
            CustomFieldsComponent,
            WorkflowComponent,
        ]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "experiments"

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/experiments/{id}/requests/applicable"),
                else_=RecordLink("{+api}/experiments/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/experiments/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/experiments/{id}/edit",
                when=has_draft() & has_permission("update"),
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/experiments/{id}/files",
                    when=has_file_permission("list_files"),
                ),
                else_=RecordLink(
                    "{+api}/experiments/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/experiments/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/experiments/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/experiments/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/experiments/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/experiments/{id}/requests"),
                else_=RecordLink("{+api}/experiments/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/experiments/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/experiments/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/experiments/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/experiments/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/experiments/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/experiments/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/experiments/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/experiments/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/experiments/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/experiments/{?args*}"),
            **pagination_links_html("{+ui}/experiments/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/experiments/{?args*}"),
            **pagination_links_html("{+ui}/user/experiments/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/experiments/{id}/versions{?args*}"),
        }
