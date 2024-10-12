from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


class ExperimentsSearchOptions(InvenioSearchOptions):
    """ExperimentsRecord search options."""

    facet_groups = {}

    facets = {
        "metadata_creators_affiliations": facets.metadata_creators_affiliations,
        "metadata_creators_authorityIdentifiers_identifier": facets.metadata_creators_authorityIdentifiers_identifier,
        "metadata_creators_authorityIdentifiers_scheme": facets.metadata_creators_authorityIdentifiers_scheme,
        "metadata_creators_familyName": facets.metadata_creators_familyName,
        "metadata_creators_fullName": facets.metadata_creators_fullName,
        "metadata_creators_givenName": facets.metadata_creators_givenName,
        "metadata_creators_nameType": facets.metadata_creators_nameType,
        "metadata_fundingReference_funder": facets.metadata_fundingReference_funder,
        "metadata_fundingReference_projectID": facets.metadata_fundingReference_projectID,
        "metadata_objectIdentifiers_identifier": facets.metadata_objectIdentifiers_identifier,
        "metadata_objectIdentifiers_scheme": facets.metadata_objectIdentifiers_scheme,
        "metadata_publisher": facets.metadata_publisher,
        "metadata_simulations__dump_sw_version": facets.metadata_simulations__dump_sw_version,
        "metadata_simulations__exit_code": facets.metadata_simulations__exit_code,
        "metadata_simulations__gromacs_version": facets.metadata_simulations__gromacs_version,
        "metadata_simulations__metadata_date": facets.metadata_simulations__metadata_date,
        "metadata_simulations__metadump_version": facets.metadata_simulations__metadump_version,
        "metadata_simulations__protein_sequences": facets.metadata_simulations__protein_sequences,
        "metadata_simulations__record_file": facets.metadata_simulations__record_file,
        "metadata_simulations__record_url": facets.metadata_simulations__record_url,
        "metadata_simulations__tpx_version": facets.metadata_simulations__tpx_version,
        "metadata_simulations__uniprot_id": facets.metadata_simulations__uniprot_id,
        "metadata_simulations_detailed_information_barostat_compressibility": facets.metadata_simulations_detailed_information_barostat_compressibility,
        "metadata_simulations_detailed_information_barostat_pcoupl": facets.metadata_simulations_detailed_information_barostat_pcoupl,
        "metadata_simulations_detailed_information_barostat_pcoupltype": facets.metadata_simulations_detailed_information_barostat_pcoupltype,
        "metadata_simulations_detailed_information_barostat_refcoord_scaling": facets.metadata_simulations_detailed_information_barostat_refcoord_scaling,
        "metadata_simulations_detailed_information_barostat_tau_p": facets.metadata_simulations_detailed_information_barostat_tau_p,
        "metadata_simulations_detailed_information_comm_mode": facets.metadata_simulations_detailed_information_comm_mode,
        "metadata_simulations_detailed_information_constraint_algorithm": facets.metadata_simulations_detailed_information_constraint_algorithm,
        "metadata_simulations_detailed_information_electrostatic_interactions_coulomb_modifier": facets.metadata_simulations_detailed_information_electrostatic_interactions_coulomb_modifier,
        "metadata_simulations_detailed_information_electrostatic_interactions_coulombtype": facets.metadata_simulations_detailed_information_electrostatic_interactions_coulombtype,
        "metadata_simulations_detailed_information_electrostatic_interactions_epsilon_r": facets.metadata_simulations_detailed_information_electrostatic_interactions_epsilon_r,
        "metadata_simulations_detailed_information_electrostatic_interactions_epsilon_rf": facets.metadata_simulations_detailed_information_electrostatic_interactions_epsilon_rf,
        "metadata_simulations_detailed_information_electrostatic_interactions_rcoulomb": facets.metadata_simulations_detailed_information_electrostatic_interactions_rcoulomb,
        "metadata_simulations_detailed_information_fourierspacing": facets.metadata_simulations_detailed_information_fourierspacing,
        "metadata_simulations_detailed_information_lincs_iter": facets.metadata_simulations_detailed_information_lincs_iter,
        "metadata_simulations_detailed_information_lincs_order": facets.metadata_simulations_detailed_information_lincs_order,
        "metadata_simulations_detailed_information_neighbour_list_cutoff_scheme": facets.metadata_simulations_detailed_information_neighbour_list_cutoff_scheme,
        "metadata_simulations_detailed_information_neighbour_list_nstlist": facets.metadata_simulations_detailed_information_neighbour_list_nstlist,
        "metadata_simulations_detailed_information_neighbour_list_pbc": facets.metadata_simulations_detailed_information_neighbour_list_pbc,
        "metadata_simulations_detailed_information_neighbour_list_rlist": facets.metadata_simulations_detailed_information_neighbour_list_rlist,
        "metadata_simulations_detailed_information_nstcomm": facets.metadata_simulations_detailed_information_nstcomm,
        "metadata_simulations_detailed_information_thermostat_nsttcouple": facets.metadata_simulations_detailed_information_thermostat_nsttcouple,
        "metadata_simulations_detailed_information_thermostat_tau_t": facets.metadata_simulations_detailed_information_thermostat_tau_t,
        "metadata_simulations_detailed_information_thermostat_tc_grps_name": facets.metadata_simulations_detailed_information_thermostat_tc_grps_name,
        "metadata_simulations_detailed_information_thermostat_tc_grps_nr": facets.metadata_simulations_detailed_information_thermostat_tc_grps_nr,
        "metadata_simulations_detailed_information_thermostat_tcoupl": facets.metadata_simulations_detailed_information_thermostat_tcoupl,
        "metadata_simulations_detailed_information_van_der_Waals_interactions_dispcorr": facets.metadata_simulations_detailed_information_van_der_Waals_interactions_dispcorr,
        "metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw": facets.metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw,
        "metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw_switch": facets.metadata_simulations_detailed_information_van_der_Waals_interactions_rvdw_switch,
        "metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_modifier": facets.metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_modifier,
        "metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_type": facets.metadata_simulations_detailed_information_van_der_Waals_interactions_vdw_type,
        "metadata_simulations_file_identification_authors": facets.metadata_simulations_file_identification_authors,
        "metadata_simulations_file_identification_doi": facets.metadata_simulations_file_identification_doi,
        "metadata_simulations_file_identification_name": facets.metadata_simulations_file_identification_name,
        "metadata_simulations_file_identification_related_files": facets.metadata_simulations_file_identification_related_files,
        "metadata_simulations_file_identification_simulation_year": facets.metadata_simulations_file_identification_simulation_year,
        "metadata_simulations_main_information_AWH_adaptive_biasing": facets.metadata_simulations_main_information_AWH_adaptive_biasing,
        "metadata_simulations_main_information_box_size_and_shape": facets.metadata_simulations_main_information_box_size_and_shape,
        "metadata_simulations_main_information_force_field": facets.metadata_simulations_main_information_force_field,
        "metadata_simulations_main_information_free_energy_calculation": facets.metadata_simulations_main_information_free_energy_calculation,
        "metadata_simulations_main_information_molecules_count": facets.metadata_simulations_main_information_molecules_count,
        "metadata_simulations_main_information_molecules_id": facets.metadata_simulations_main_information_molecules_id,
        "metadata_simulations_main_information_molecules_name": facets.metadata_simulations_main_information_molecules_name,
        "metadata_simulations_main_information_molecules_residues": facets.metadata_simulations_main_information_molecules_residues,
        "metadata_simulations_main_information_reference_pressure": facets.metadata_simulations_main_information_reference_pressure,
        "metadata_simulations_main_information_reference_temperature": facets.metadata_simulations_main_information_reference_temperature,
        "metadata_simulations_main_information_simulation_length": facets.metadata_simulations_main_information_simulation_length,
        "metadata_simulations_main_information_simulation_time_step": facets.metadata_simulations_main_information_simulation_time_step,
        "metadata_simulations_main_information_simulation_type": facets.metadata_simulations_main_information_simulation_type,
        "metadata_simulations_main_information_statistical_ensamble": facets.metadata_simulations_main_information_statistical_ensamble,
        "metadata_simulations_main_information_umbrella_sampling": facets.metadata_simulations_main_information_umbrella_sampling,
        "metadata_version": facets.metadata_version,
        **getattr(InvenioSearchOptions, "facets", {}),
        "record_status": facets.record_status,
        "has_draft": facets.has_draft,
    }
