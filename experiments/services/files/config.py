from invenio_records_resources.services import (
    FileLink,
    FileServiceConfig,
    LinksTemplate,
    RecordLink,
)
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_file_permission,
    has_permission_file_service,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.services.files.schema import ExperimentsFileSchema
from experiments.services.records.permissions import ExperimentsPermissionPolicy
from shared.services.files import CompChemFilesServiceConfig


class ExperimentsFileServiceConfig(CompChemFilesServiceConfig):
    """ExperimentsRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/experiments/<pid_value>"

    base_permission_policy_cls = ExperimentsPermissionPolicy

    schema = ExperimentsFileSchema

    record_cls = ExperimentsRecord

    service_id = "experiments_file"

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
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
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/experiments/{id}/files",
                when=has_permission_file_service("list_files"),
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/experiments/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/experiments/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/experiments/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/experiments/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }


class ExperimentsFileDraftServiceConfig(
    PermissionsPresetsConfigMixin, FileServiceConfig
):
    """ExperimentsDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/experiments/<pid_value>/draft"

    schema = ExperimentsFileSchema

    record_cls = ExperimentsDraft

    service_id = "experiments_file_draft"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
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
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/experiments/{id}/draft/files",
                when=has_file_permission("list_files"),
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/experiments/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/experiments/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/experiments/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/experiments/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
