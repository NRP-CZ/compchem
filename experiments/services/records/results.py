from oarepo_requests.services.results import RequestsComponent, RequestTypesComponent
from oarepo_runtime.services.results import RecordItem, RecordList


class ExperimentsRecordItem(RecordItem):
    """ExperimentsRecord record item."""

    components = [*RecordItem.components, RequestsComponent(), RequestTypesComponent()]


class ExperimentsRecordList(RecordList):
    """ExperimentsRecord record list."""

    components = [*RecordList.components]
