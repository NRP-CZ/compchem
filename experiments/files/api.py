from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from experiments.files.models import (
    ExperimentsFileDraftMetadata,
    ExperimentsFileMetadata,
)


class ExperimentsFile(FileRecord):

    model_cls = ExperimentsFileMetadata

    index = IndexField(
        "experiments_file-experiments_file-1.0.0",
    )
    record_cls = None  # is defined inside the parent record


class ExperimentsFileDraft(FileRecord):

    model_cls = ExperimentsFileDraftMetadata

    index = IndexField(
        "experiments_file_draft-experiments_file_draft-1.0.0",
    )
    record_cls = None  # is defined inside the parent record
