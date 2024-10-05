from invenio_records_resources.services import FileLink, FileServiceConfig, RecordLink
from oarepo_runtime.services.components import CustomFieldsComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from experiments.records.api import ExperimentsDraft, ExperimentsRecord
from experiments.services.files.schema import ExperimentsFileSchema
from experiments.services.records.permissions import ExperimentsPermissionPolicy
from shared.services.files import CompChemFilesServiceConfig


class ExperimentsFileServiceConfig(CompChemFilesServiceConfig):
    """ExperimentsRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/experiments/<pid_value>"

    base_permission_policy_cls = ExperimentsPermissionPolicy

    schema = ExperimentsFileSchema

    record_cls = ExperimentsRecord

    service_id = "experiments_file"

    components = [*CompChemFilesServiceConfig.components, CustomFieldsComponent]

    model = "experiments"
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/experiments/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/experiments/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/experiments/{id}/files/{key}/content"),
            "preview": FileLink("{+ui}/experiments/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/experiments/{id}/files/{key}"),
        }


class ExperimentsFileDraftServiceConfig(
    PermissionsPresetsConfigMixin, FileServiceConfig
):
    """ExperimentsDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/experiments/<pid_value>/draft"

    schema = ExperimentsFileSchema

    record_cls = ExperimentsDraft

    service_id = "experiments_file_draft"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *FileServiceConfig.components,
        CustomFieldsComponent,
    ]

    model = "experiments"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/experiments/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/experiments/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/experiments/{id}/draft/files/{key}/content"),
            "preview": FileLink("{+ui}/experiments/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/experiments/{id}/draft/files/{key}"),
        }
