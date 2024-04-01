from invenio_records_resources.services import FileServiceConfig
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from .processors import ExtractTPRParametersProcessor


class CompChemFilesServiceConfig(PermissionsPresetsConfigMixin, FileServiceConfig):
    file_processors = [
        ExtractTPRParametersProcessor(),
    ]
