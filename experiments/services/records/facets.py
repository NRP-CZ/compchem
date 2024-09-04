"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet
from oarepo_vocabularies.services.facets import (
    HierarchyVocabularyFacet,
    VocabularyFacet,
)

metadata_creators_affiliations = HierarchyVocabularyFacet(
    field="metadata.creators.affiliations",
    label=_("metadata/creators/affiliations.label"),
    vocabulary="institutions",
)

metadata_creators_authorityIdentifiers_identifier = TermsFacet(
    field="metadata.creators.authorityIdentifiers.identifier",
    label=_("metadata/creators/authorityIdentifiers/identifier.label"),
)

metadata_creators_authorityIdentifiers_scheme = TermsFacet(
    field="metadata.creators.authorityIdentifiers.scheme",
    label=_("metadata/creators/authorityIdentifiers/scheme.label"),
)

metadata_creators_familyName = TermsFacet(
    field="metadata.creators.familyName", label=_("metadata/creators/familyName.label")
)

metadata_creators_fullName = TermsFacet(
    field="metadata.creators.fullName", label=_("metadata/creators/fullName.label")
)

metadata_creators_givenName = TermsFacet(
    field="metadata.creators.givenName", label=_("metadata/creators/givenName.label")
)

metadata_creators_nameType = TermsFacet(
    field="metadata.creators.nameType", label=_("metadata/creators/nameType.label")
)

metadata_fundingReference_funder = VocabularyFacet(
    field="metadata.fundingReference.funder",
    label=_("metadata/fundingReference/funder.label"),
    vocabulary="funders",
)

metadata_fundingReference_projectID = TermsFacet(
    field="metadata.fundingReference.projectID",
    label=_("metadata/fundingReference/projectID.label"),
)

metadata_objectIdentifiers_identifier = TermsFacet(
    field="metadata.objectIdentifiers.identifier",
    label=_("metadata/objectIdentifiers/identifier.label"),
)

metadata_objectIdentifiers_scheme = TermsFacet(
    field="metadata.objectIdentifiers.scheme",
    label=_("metadata/objectIdentifiers/scheme.label"),
)

metadata_publisher = TermsFacet(
    field="metadata.publisher", label=_("metadata/publisher.label")
)

metadata_simulations__dump_sw_version = TermsFacet(
    field="metadata.simulations._dump_sw_version",
    label=_("metadata/simulations/_dump_sw_version.label"),
)

metadata_simulations__gromacs_version = TermsFacet(
    field="metadata.simulations._gromacs_version",
    label=_("metadata/simulations/_gromacs_version.label"),
)

metadata_simulations__metadata_date = DateTimeFacet(
    field="metadata.simulations._metadata_date",
    label=_("metadata/simulations/_metadata_date.label"),
)

metadata_simulations__record_file = TermsFacet(
    field="metadata.simulations._record_file",
    label=_("metadata/simulations/_record_file.label"),
)

metadata_simulations__record_url = TermsFacet(
    field="metadata.simulations._record_url",
    label=_("metadata/simulations/_record_url.label"),
)

metadata_simulations__tpr_date = DateTimeFacet(
    field="metadata.simulations._tpr_date",
    label=_("metadata/simulations/_tpr_date.label"),
)

metadata_simulations__tpx_version = TermsFacet(
    field="metadata.simulations._tpx_version",
    label=_("metadata/simulations/_tpx_version.label"),
)

metadata_simulations__uniprot_id = TermsFacet(
    field="metadata.simulations._uniprot_id",
    label=_("metadata/simulations/_uniprot_id.label"),
)

metadata_simulations_detailed_information_barostat_compressibility = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.compressibility",
    label=_("metadata/simulations/detailed_information/barostat/compressibility.label"),
)

metadata_simulations_detailed_information_barostat_pcoupl = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.pcoupl",
    label=_("metadata/simulations/detailed_information/barostat/pcoupl.label"),
)

metadata_simulations_detailed_information_barostat_refcoord_scaling = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.refcoord-scaling",
    label=_(
        "metadata/simulations/detailed_information/barostat/refcoord-scaling.label"
    ),
)

metadata_simulations_detailed_information_barostat_tau_p = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.tau-p",
    label=_("metadata/simulations/detailed_information/barostat/tau-p.label"),
)

metadata_simulations_detailed_information_comm_mode = TermsFacet(
    field="metadata.simulations.detailed_information.comm-mode",
    label=_("metadata/simulations/detailed_information/comm-mode.label"),
)

metadata_simulations_detailed_information_constraint_algorithm = TermsFacet(
    field="metadata.simulations.detailed_information.constraint-algorithm",
    label=_("metadata/simulations/detailed_information/constraint-algorithm.label"),
)

metadata_simulations_detailed_information_electrostatic_interactions_coulomb_modifier = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.coulomb-modifier",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/coulomb-modifier.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_epsilon_r = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.epsilon-r",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/epsilon-r.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_epsilon_rf = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.epsilon-rf",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/epsilon-rf.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_rcoulomb = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.rcoulomb",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/rcoulomb.label"
    ),
)

metadata_simulations_detailed_information_fourierspacing = TermsFacet(
    field="metadata.simulations.detailed_information.fourierspacing",
    label=_("metadata/simulations/detailed_information/fourierspacing.label"),
)

metadata_simulations_detailed_information_lincs_iter = TermsFacet(
    field="metadata.simulations.detailed_information.lincs-iter",
    label=_("metadata/simulations/detailed_information/lincs-iter.label"),
)

metadata_simulations_detailed_information_lincs_order = TermsFacet(
    field="metadata.simulations.detailed_information.lincs-order",
    label=_("metadata/simulations/detailed_information/lincs-order.label"),
)

metadata_simulations_detailed_information_neighbour_list_cutoff_scheme = TermsFacet(
    field="metadata.simulations.detailed_information.neighbour_list.cutoff-scheme",
    label=_(
        "metadata/simulations/detailed_information/neighbour_list/cutoff-scheme.label"
    ),
)

metadata_simulations_detailed_information_neighbour_list_nstlist = TermsFacet(
    field="metadata.simulations.detailed_information.neighbour_list.nstlist",
    label=_("metadata/simulations/detailed_information/neighbour_list/nstlist.label"),
)

metadata_simulations_detailed_information_neighbour_list_pbc = TermsFacet(
    field="metadata.simulations.detailed_information.neighbour_list.pbc",
    label=_("metadata/simulations/detailed_information/neighbour_list/pbc.label"),
)

metadata_simulations_detailed_information_neighbour_list_rlist = TermsFacet(
    field="metadata.simulations.detailed_information.neighbour_list.rlist",
    label=_("metadata/simulations/detailed_information/neighbour_list/rlist.label"),
)

metadata_simulations_detailed_information_nstcomm = TermsFacet(
    field="metadata.simulations.detailed_information.nstcomm",
    label=_("metadata/simulations/detailed_information/nstcomm.label"),
)

metadata_simulations_detailed_information_thermostat_nsttcouple = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.nsttcouple",
    label=_("metadata/simulations/detailed_information/thermostat/nsttcouple.label"),
)

metadata_simulations_detailed_information_thermostat_tau_t = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tau-t",
    label=_("metadata/simulations/detailed_information/thermostat/tau-t.label"),
)

metadata_simulations_detailed_information_thermostat_tc_grps_name = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tc-grps.name",
    label=_("metadata/simulations/detailed_information/thermostat/tc-grps/name.label"),
)

metadata_simulations_detailed_information_thermostat_tc_grps_nr = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tc-grps.nr",
    label=_("metadata/simulations/detailed_information/thermostat/tc-grps/nr.label"),
)

metadata_simulations_detailed_information_thermostat_tcoupl = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tcoupl",
    label=_("metadata/simulations/detailed_information/thermostat/tcoupl.label"),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_dispcorr = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.dispcorr",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/dispcorr.label"
    ),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.rvdw",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/rvdw.label"
    ),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw_switch = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.rvdw-switch",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/rvdw-switch.label"
    ),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_modifier = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.vdw-modifier",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/vdw-modifier.label"
    ),
)

metadata_simulations_file_identification_authors = TermsFacet(
    field="metadata.simulations.file_identification.authors",
    label=_("metadata/simulations/file_identification/authors.label"),
)

metadata_simulations_file_identification_doi = TermsFacet(
    field="metadata.simulations.file_identification.doi",
    label=_("metadata/simulations/file_identification/doi.label"),
)

metadata_simulations_file_identification_name = TermsFacet(
    field="metadata.simulations.file_identification.name",
    label=_("metadata/simulations/file_identification/name.label"),
)

metadata_simulations_file_identification_related_files = TermsFacet(
    field="metadata.simulations.file_identification.related_files",
    label=_("metadata/simulations/file_identification/related_files.label"),
)

metadata_simulations_file_identification_simulation_year = TermsFacet(
    field="metadata.simulations.file_identification.simulation_year",
    label=_("metadata/simulations/file_identification/simulation_year.label"),
)

metadata_simulations_main_information_AWH_adaptive_biasing = TermsFacet(
    field="metadata.simulations.main_information.AWH_adaptive_biasing",
    label=_("metadata/simulations/main_information/AWH_adaptive_biasing.label"),
)

metadata_simulations_main_information_box_size_and_shape = TermsFacet(
    field="metadata.simulations.main_information.box_size_and_shape",
    label=_("metadata/simulations/main_information/box_size_and_shape.label"),
)

metadata_simulations_main_information_force_field = TermsFacet(
    field="metadata.simulations.main_information.force_field",
    label=_("metadata/simulations/main_information/force_field.label"),
)

metadata_simulations_main_information_free_energy_calculation = TermsFacet(
    field="metadata.simulations.main_information.free_energy_calculation",
    label=_("metadata/simulations/main_information/free_energy_calculation.label"),
)

metadata_simulations_main_information_molecules_count = TermsFacet(
    field="metadata.simulations.main_information.molecules.count",
    label=_("metadata/simulations/main_information/molecules/count.label"),
)

metadata_simulations_main_information_molecules_id = TermsFacet(
    field="metadata.simulations.main_information.molecules.id",
    label=_("metadata/simulations/main_information/molecules/id.label"),
)

metadata_simulations_main_information_molecules_name = TermsFacet(
    field="metadata.simulations.main_information.molecules.name",
    label=_("metadata/simulations/main_information/molecules/name.label"),
)

metadata_simulations_main_information_reference_pressure = TermsFacet(
    field="metadata.simulations.main_information.reference_pressure",
    label=_("metadata/simulations/main_information/reference_pressure.label"),
)

metadata_simulations_main_information_reference_temperature = TermsFacet(
    field="metadata.simulations.main_information.reference_temperature",
    label=_("metadata/simulations/main_information/reference_temperature.label"),
)

metadata_simulations_main_information_simulation_length = TermsFacet(
    field="metadata.simulations.main_information.simulation_length",
    label=_("metadata/simulations/main_information/simulation_length.label"),
)

metadata_simulations_main_information_simulation_time_step = TermsFacet(
    field="metadata.simulations.main_information.simulation_time_step",
    label=_("metadata/simulations/main_information/simulation_time_step.label"),
)

metadata_simulations_main_information_simulation_type = TermsFacet(
    field="metadata.simulations.main_information.simulation_type",
    label=_("metadata/simulations/main_information/simulation_type.label"),
)

metadata_simulations_main_information_statistical_ensamble = TermsFacet(
    field="metadata.simulations.main_information.statistical_ensamble",
    label=_("metadata/simulations/main_information/statistical_ensamble.label"),
)

metadata_simulations_main_information_umbrella_sampling = TermsFacet(
    field="metadata.simulations.main_information.umbrella_sampling",
    label=_("metadata/simulations/main_information/umbrella_sampling.label"),
)


record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))
