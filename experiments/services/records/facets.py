"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet

metadata_creators_affiliation = TermsFacet(
    field="metadata.creators.affiliation",
    label=_("metadata/creators/affiliation.label"),
)

metadata_creators_name = TermsFacet(
    field="metadata.creators.name", label=_("metadata/creators/name.label")
)

metadata_creators_orcid = TermsFacet(
    field="metadata.creators.orcid", label=_("metadata/creators/orcid.label")
)

metadata_fundingReference_awardNumber = TermsFacet(
    field="metadata.fundingReference.awardNumber",
    label=_("metadata/fundingReference/awardNumber.label"),
)

metadata_fundingReference_funderIdentifier = TermsFacet(
    field="metadata.fundingReference.funderIdentifier",
    label=_("metadata/fundingReference/funderIdentifier.label"),
)

metadata_fundingReference_funderName = TermsFacet(
    field="metadata.fundingReference.funderName",
    label=_("metadata/fundingReference/funderName.label"),
)

metadata_objectIdentifiers_identifier = TermsFacet(
    field="metadata.objectIdentifiers.identifier",
    label=_("metadata/objectIdentifiers/identifier.label"),
)

metadata_objectIdentifiers_identifierType = TermsFacet(
    field="metadata.objectIdentifiers.identifierType",
    label=_("metadata/objectIdentifiers/identifierType.label"),
)

metadata_publisher = TermsFacet(
    field="metadata.publisher", label=_("metadata/publisher.label")
)

metadata_simulations__dump_sw_version = TermsFacet(
    field="metadata.simulations._dump_sw_version",
    label=_("metadata/simulations/_dump_sw_version.label"),
)

metadata_simulations__exit_code = TermsFacet(
    field="metadata.simulations._exit_code",
    label=_("metadata/simulations/_exit_code.label"),
)

metadata_simulations__gromacs_version = TermsFacet(
    field="metadata.simulations._gromacs_version",
    label=_("metadata/simulations/_gromacs_version.label"),
)

metadata_simulations__metadata_date = DateTimeFacet(
    field="metadata.simulations._metadata_date",
    label=_("metadata/simulations/_metadata_date.label"),
)

metadata_simulations__metadump_version = TermsFacet(
    field="metadata.simulations._metadump_version",
    label=_("metadata/simulations/_metadump_version.label"),
)

metadata_simulations__protein_sequences = TermsFacet(
    field="metadata.simulations._protein_sequences",
    label=_("metadata/simulations/_protein_sequences.label"),
)

metadata_simulations__record_file = TermsFacet(
    field="metadata.simulations._record_file",
    label=_("metadata/simulations/_record_file.label"),
)

metadata_simulations__record_url = TermsFacet(
    field="metadata.simulations._record_url",
    label=_("metadata/simulations/_record_url.label"),
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

metadata_simulations_detailed_information_barostat_pcoupltype = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.pcoupltype",
    label=_("metadata/simulations/detailed_information/barostat/pcoupltype.label"),
)

metadata_simulations_detailed_information_barostat_refcoord_scaling = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.refcoord_scaling",
    label=_(
        "metadata/simulations/detailed_information/barostat/refcoord_scaling.label"
    ),
)

metadata_simulations_detailed_information_barostat_tau_p = TermsFacet(
    field="metadata.simulations.detailed_information.barostat.tau_p",
    label=_("metadata/simulations/detailed_information/barostat/tau_p.label"),
)

metadata_simulations_detailed_information_comm_mode = TermsFacet(
    field="metadata.simulations.detailed_information.comm_mode",
    label=_("metadata/simulations/detailed_information/comm_mode.label"),
)

metadata_simulations_detailed_information_constraint_algorithm = TermsFacet(
    field="metadata.simulations.detailed_information.constraint_algorithm",
    label=_("metadata/simulations/detailed_information/constraint_algorithm.label"),
)

metadata_simulations_detailed_information_electrostatic_interactions_coulomb_modifier = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.coulomb_modifier",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/coulomb_modifier.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_coulombtype = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.coulombtype",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/coulombtype.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_epsilon_r = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.epsilon_r",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/epsilon_r.label"
    ),
)

metadata_simulations_detailed_information_electrostatic_interactions_epsilon_rf = TermsFacet(
    field="metadata.simulations.detailed_information.electrostatic_interactions.epsilon_rf",
    label=_(
        "metadata/simulations/detailed_information/electrostatic_interactions/epsilon_rf.label"
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
    field="metadata.simulations.detailed_information.lincs_iter",
    label=_("metadata/simulations/detailed_information/lincs_iter.label"),
)

metadata_simulations_detailed_information_lincs_order = TermsFacet(
    field="metadata.simulations.detailed_information.lincs_order",
    label=_("metadata/simulations/detailed_information/lincs_order.label"),
)

metadata_simulations_detailed_information_neighbour_list_cutoff_scheme = TermsFacet(
    field="metadata.simulations.detailed_information.neighbour_list.cutoff_scheme",
    label=_(
        "metadata/simulations/detailed_information/neighbour_list/cutoff_scheme.label"
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
    field="metadata.simulations.detailed_information.thermostat.tau_t",
    label=_("metadata/simulations/detailed_information/thermostat/tau_t.label"),
)

metadata_simulations_detailed_information_thermostat_tc_grps_name = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tc_grps.name",
    label=_("metadata/simulations/detailed_information/thermostat/tc_grps/name.label"),
)

metadata_simulations_detailed_information_thermostat_tc_grps_nr = TermsFacet(
    field="metadata.simulations.detailed_information.thermostat.tc_grps.nr",
    label=_("metadata/simulations/detailed_information/thermostat/tc_grps/nr.label"),
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
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.rvdw_switch",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/rvdw_switch.label"
    ),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_modifier = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.vdw_modifier",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/vdw_modifier.label"
    ),
)

metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_type = TermsFacet(
    field="metadata.simulations.detailed_information.van_der_Waals_interactions.vdw_type",
    label=_(
        "metadata/simulations/detailed_information/van_der_Waals_interactions/vdw_type.label"
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

metadata_simulations_main_information_molecules_residues = TermsFacet(
    field="metadata.simulations.main_information.molecules.residues",
    label=_("metadata/simulations/main_information/molecules/residues.label"),
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

metadata_version = TermsFacet(
    field="metadata.version", label=_("metadata/version.label")
)

state = TermsFacet(field="state", label=_("state.label"))

state_timestamp = DateTimeFacet(
    field="state_timestamp", label=_("state_timestamp.label")
)


record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))
