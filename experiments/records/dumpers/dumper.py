from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from experiments.records.dumpers.edtf import (
    ExperimentsDraftEDTFIntervalDumperExt,
    ExperimentsEDTFIntervalDumperExt,
)
from experiments.records.dumpers.multilingual import MultilingualSearchDumperExt


class ExperimentsDumper(SearchDumper):
    """ExperimentsRecord opensearch dumper."""

    extensions = [
        SystemFieldDumperExt(),
        MultilingualSearchDumperExt(),
        ExperimentsEDTFIntervalDumperExt(),
    ]


class ExperimentsDraftDumper(SearchDumper):
    """ExperimentsDraft opensearch dumper."""

    extensions = [
        SystemFieldDumperExt(),
        MultilingualSearchDumperExt(),
        ExperimentsDraftEDTFIntervalDumperExt(),
    ]
