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

metadata_simulations_detailedInformation_barostat_compressibility = TermsFacet(
    field="metadata.simulations.detailedInformation.barostat.compressibility",
    label=_("metadata/simulations/detailedInformation/barostat/compressibility.label"),
)

metadata_simulations_detailedInformation_barostat_pcoupl = TermsFacet(
    field="metadata.simulations.detailedInformation.barostat.pcoupl",
    label=_("metadata/simulations/detailedInformation/barostat/pcoupl.label"),
)

metadata_simulations_detailedInformation_barostat_refcoordScaling = TermsFacet(
    field="metadata.simulations.detailedInformation.barostat.refcoordScaling",
    label=_("metadata/simulations/detailedInformation/barostat/refcoordScaling.label"),
)

metadata_simulations_detailedInformation_barostat_tauP = TermsFacet(
    field="metadata.simulations.detailedInformation.barostat.tauP",
    label=_("metadata/simulations/detailedInformation/barostat/tauP.label"),
)

metadata_simulations_detailedInformation_commMode = TermsFacet(
    field="metadata.simulations.detailedInformation.commMode",
    label=_("metadata/simulations/detailedInformation/commMode.label"),
)

metadata_simulations_detailedInformation_constraintAlgorithm = TermsFacet(
    field="metadata.simulations.detailedInformation.constraintAlgorithm",
    label=_("metadata/simulations/detailedInformation/constraintAlgorithm.label"),
)

metadata_simulations_detailedInformation_electrostaticInteractions_coulombModifier = TermsFacet(
    field="metadata.simulations.detailedInformation.electrostaticInteractions.coulombModifier",
    label=_(
        "metadata/simulations/detailedInformation/electrostaticInteractions/coulombModifier.label"
    ),
)

metadata_simulations_detailedInformation_electrostaticInteractions_epsilonR = TermsFacet(
    field="metadata.simulations.detailedInformation.electrostaticInteractions.epsilonR",
    label=_(
        "metadata/simulations/detailedInformation/electrostaticInteractions/epsilonR.label"
    ),
)

metadata_simulations_detailedInformation_electrostaticInteractions_epsilonRF = TermsFacet(
    field="metadata.simulations.detailedInformation.electrostaticInteractions.epsilonRF",
    label=_(
        "metadata/simulations/detailedInformation/electrostaticInteractions/epsilonRF.label"
    ),
)

metadata_simulations_detailedInformation_electrostaticInteractions_rcoulomb = TermsFacet(
    field="metadata.simulations.detailedInformation.electrostaticInteractions.rcoulomb",
    label=_(
        "metadata/simulations/detailedInformation/electrostaticInteractions/rcoulomb.label"
    ),
)

metadata_simulations_detailedInformation_fourierSpacing = TermsFacet(
    field="metadata.simulations.detailedInformation.fourierSpacing",
    label=_("metadata/simulations/detailedInformation/fourierSpacing.label"),
)

metadata_simulations_detailedInformation_lincsIter = TermsFacet(
    field="metadata.simulations.detailedInformation.lincsIter",
    label=_("metadata/simulations/detailedInformation/lincsIter.label"),
)

metadata_simulations_detailedInformation_lincsOrder = TermsFacet(
    field="metadata.simulations.detailedInformation.lincsOrder",
    label=_("metadata/simulations/detailedInformation/lincsOrder.label"),
)

metadata_simulations_detailedInformation_neighbourList_cutoffScheme = TermsFacet(
    field="metadata.simulations.detailedInformation.neighbourList.cutoffScheme",
    label=_(
        "metadata/simulations/detailedInformation/neighbourList/cutoffScheme.label"
    ),
)

metadata_simulations_detailedInformation_neighbourList_nstlist = TermsFacet(
    field="metadata.simulations.detailedInformation.neighbourList.nstlist",
    label=_("metadata/simulations/detailedInformation/neighbourList/nstlist.label"),
)

metadata_simulations_detailedInformation_neighbourList_pbc = TermsFacet(
    field="metadata.simulations.detailedInformation.neighbourList.pbc",
    label=_("metadata/simulations/detailedInformation/neighbourList/pbc.label"),
)

metadata_simulations_detailedInformation_neighbourList_rlist = TermsFacet(
    field="metadata.simulations.detailedInformation.neighbourList.rlist",
    label=_("metadata/simulations/detailedInformation/neighbourList/rlist.label"),
)

metadata_simulations_detailedInformation_nstcomm = TermsFacet(
    field="metadata.simulations.detailedInformation.nstcomm",
    label=_("metadata/simulations/detailedInformation/nstcomm.label"),
)

metadata_simulations_detailedInformation_thermostat_nsttcouple = TermsFacet(
    field="metadata.simulations.detailedInformation.thermostat.nsttcouple",
    label=_("metadata/simulations/detailedInformation/thermostat/nsttcouple.label"),
)

metadata_simulations_detailedInformation_thermostat_tauT = TermsFacet(
    field="metadata.simulations.detailedInformation.thermostat.tauT",
    label=_("metadata/simulations/detailedInformation/thermostat/tauT.label"),
)

metadata_simulations_detailedInformation_thermostat_tcGrps_name = TermsFacet(
    field="metadata.simulations.detailedInformation.thermostat.tcGrps.name",
    label=_("metadata/simulations/detailedInformation/thermostat/tcGrps/name.label"),
)

metadata_simulations_detailedInformation_thermostat_tcGrps_nr = TermsFacet(
    field="metadata.simulations.detailedInformation.thermostat.tcGrps.nr",
    label=_("metadata/simulations/detailedInformation/thermostat/tcGrps/nr.label"),
)

metadata_simulations_detailedInformation_thermostat_tcoupl = TermsFacet(
    field="metadata.simulations.detailedInformation.thermostat.tcoupl",
    label=_("metadata/simulations/detailedInformation/thermostat/tcoupl.label"),
)

metadata_simulations_detailedInformation_vanDerWaalsInteractions_dispcorr = TermsFacet(
    field="metadata.simulations.detailedInformation.vanDerWaalsInteractions.dispcorr",
    label=_(
        "metadata/simulations/detailedInformation/vanDerWaalsInteractions/dispcorr.label"
    ),
)

metadata_simulations_detailedInformation_vanDerWaalsInteractions_rvdw = TermsFacet(
    field="metadata.simulations.detailedInformation.vanDerWaalsInteractions.rvdw",
    label=_(
        "metadata/simulations/detailedInformation/vanDerWaalsInteractions/rvdw.label"
    ),
)

metadata_simulations_detailedInformation_vanDerWaalsInteractions_rvdwSwitch = TermsFacet(
    field="metadata.simulations.detailedInformation.vanDerWaalsInteractions.rvdwSwitch",
    label=_(
        "metadata/simulations/detailedInformation/vanDerWaalsInteractions/rvdwSwitch.label"
    ),
)

metadata_simulations_detailedInformation_vanDerWaalsInteractions_vdwModifier = TermsFacet(
    field="metadata.simulations.detailedInformation.vanDerWaalsInteractions.vdwModifier",
    label=_(
        "metadata/simulations/detailedInformation/vanDerWaalsInteractions/vdwModifier.label"
    ),
)

metadata_simulations_key = TermsFacet(
    field="metadata.simulations.key", label=_("metadata/simulations/key.label")
)

metadata_simulations_mainInformation_AWHAdaptiveBiasing = TermsFacet(
    field="metadata.simulations.mainInformation.AWHAdaptiveBiasing",
    label=_("metadata/simulations/mainInformation/AWHAdaptiveBiasing.label"),
)

metadata_simulations_mainInformation_boxSizeAndShape = TermsFacet(
    field="metadata.simulations.mainInformation.boxSizeAndShape",
    label=_("metadata/simulations/mainInformation/boxSizeAndShape.label"),
)

metadata_simulations_mainInformation_forceField = TermsFacet(
    field="metadata.simulations.mainInformation.forceField",
    label=_("metadata/simulations/mainInformation/forceField.label"),
)

metadata_simulations_mainInformation_freeEnergyCalculation = TermsFacet(
    field="metadata.simulations.mainInformation.freeEnergyCalculation",
    label=_("metadata/simulations/mainInformation/freeEnergyCalculation.label"),
)

metadata_simulations_mainInformation_molecules_count = TermsFacet(
    field="metadata.simulations.mainInformation.molecules.count",
    label=_("metadata/simulations/mainInformation/molecules/count.label"),
)

metadata_simulations_mainInformation_molecules_id = TermsFacet(
    field="metadata.simulations.mainInformation.molecules.id",
    label=_("metadata/simulations/mainInformation/molecules/id.label"),
)

metadata_simulations_mainInformation_molecules_name = TermsFacet(
    field="metadata.simulations.mainInformation.molecules.name",
    label=_("metadata/simulations/mainInformation/molecules/name.label"),
)

metadata_simulations_mainInformation_referencePressure = TermsFacet(
    field="metadata.simulations.mainInformation.referencePressure",
    label=_("metadata/simulations/mainInformation/referencePressure.label"),
)

metadata_simulations_mainInformation_referenceTemperature = TermsFacet(
    field="metadata.simulations.mainInformation.referenceTemperature",
    label=_("metadata/simulations/mainInformation/referenceTemperature.label"),
)

metadata_simulations_mainInformation_simulationLength = TermsFacet(
    field="metadata.simulations.mainInformation.simulationLength",
    label=_("metadata/simulations/mainInformation/simulationLength.label"),
)

metadata_simulations_mainInformation_simulationTimeStep = TermsFacet(
    field="metadata.simulations.mainInformation.simulationTimeStep",
    label=_("metadata/simulations/mainInformation/simulationTimeStep.label"),
)

metadata_simulations_mainInformation_simulationType = TermsFacet(
    field="metadata.simulations.mainInformation.simulationType",
    label=_("metadata/simulations/mainInformation/simulationType.label"),
)

metadata_simulations_mainInformation_statisticalEnsemble = TermsFacet(
    field="metadata.simulations.mainInformation.statisticalEnsemble",
    label=_("metadata/simulations/mainInformation/statisticalEnsemble.label"),
)

metadata_simulations_mainInformation_umbrellaSampling = TermsFacet(
    field="metadata.simulations.mainInformation.umbrellaSampling",
    label=_("metadata/simulations/mainInformation/umbrellaSampling.label"),
)

metadata_simulations_relatedFiles_key = TermsFacet(
    field="metadata.simulations.relatedFiles.key",
    label=_("metadata/simulations/relatedFiles/key.label"),
)

metadata_simulations_simulationYear = TermsFacet(
    field="metadata.simulations.simulationYear",
    label=_("metadata/simulations/simulationYear.label"),
)

metadata_simulations_software_extractorVersion = TermsFacet(
    field="metadata.simulations.software.extractorVersion",
    label=_("metadata/simulations/software/extractorVersion.label"),
)

metadata_simulations_software_gromacsVersion = TermsFacet(
    field="metadata.simulations.software.gromacsVersion",
    label=_("metadata/simulations/software/gromacsVersion.label"),
)

metadata_simulations_software_tpxVersion = TermsFacet(
    field="metadata.simulations.software.tpxVersion",
    label=_("metadata/simulations/software/tpxVersion.label"),
)

metadata_simulations_timestamps_metadataExtractionTimestamp = DateTimeFacet(
    field="metadata.simulations.timestamps.metadataExtractionTimestamp",
    label=_("metadata/simulations/timestamps/metadataExtractionTimestamp.label"),
)

metadata_simulations_timestamps_tprFileTimestamp = DateTimeFacet(
    field="metadata.simulations.timestamps.tprFileTimestamp",
    label=_("metadata/simulations/timestamps/tprFileTimestamp.label"),
)
