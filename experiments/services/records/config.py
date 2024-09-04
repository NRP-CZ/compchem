from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.services.records.permissions import ExperimentsPermissionPolicy
from experiments.services.records.results import (
    ExperimentsRecordItem,
    ExperimentsRecordList,
)
from experiments.services.records.schema import ExperimentsSchema
from experiments.services.records.search import ExperimentsSearchOptions
from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import CustomFieldsComponent, OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent


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

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        OwnersComponent,
        FilesComponent,
        CustomFieldsComponent,
        DraftFilesComponent,
    ]

    model = "experiments"
    draft_cls = ExperimentsDraft
    search_drafts = ExperimentsSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/experiments/{id}/requests/applicable"),
                else_=RecordLink("{+api}/experiments/{id}/draft/requests/applicable"),
            ),
            "draft": RecordLink("{+api}/experiments/{id}/draft"),
            "edit_html": RecordLink("{+ui}/experiments/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/experiments/{id}/files"),
                else_=RecordLink("{+api}/experiments/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/experiments/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/experiments/{id}/latest"),
            "publish": RecordLink("{+api}/experiments/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/experiments/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/experiments/{id}/requests"),
                else_=RecordLink("{+api}/experiments/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/experiments/{id}"),
                else_=RecordLink("{+api}/experiments/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/experiments/{id}"),
                else_=RecordLink("{+ui}/experiments/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/experiments/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/experiments/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/experiments/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/experiments/{id}/versions{?args*}"),
        }
