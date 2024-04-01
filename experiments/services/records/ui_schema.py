import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from nr_metadata.common.services.records.ui_schema_datatypes import (
    NRCreatorUISchema,
    NRFundingReferenceUISchema,
)
from nr_metadata.ui_schema.identifiers import NRObjectIdentifierUISchema
from oarepo_requests.services.ui_schema import UIRequestsSerializationMixin
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema, LocalizedDateTime


class ExperimentsUISchema(UIRequestsSerializationMixin, InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: ExperimentsMetadataUISchema())


class ExperimentsMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    creators = ma_fields.List(ma_fields.Nested(lambda: NRCreatorUISchema()))

    description = ma_fields.String()

    fundingReference = ma_fields.Nested(lambda: NRFundingReferenceUISchema())

    name = ma_fields.String()

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierUISchema())
    )

    publisher = ma_fields.String()

    simulations = ma_fields.List(ma_fields.Nested(lambda: SimulationsItemUISchema()))


class SimulationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    detailedInformation = ma_fields.Nested(lambda: DetailedInformationUISchema())

    key = ma_fields.String()

    mainInformation = ma_fields.Nested(lambda: MainInformationUISchema())

    relatedFiles = ma_fields.List(ma_fields.Nested(lambda: RelatedFilesItemUISchema()))

    simulationYear = ma_fields.Integer()

    software = ma_fields.Nested(lambda: SoftwareUISchema())

    timestamps = ma_fields.Nested(lambda: TimestampsUISchema())


class DetailedInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    barostat = ma_fields.Nested(lambda: BarostatUISchema())

    commMode = ma_fields.String(
        validate=[
            OneOf(["Linear", "Angular", "Linear-acceleration-correction", "None"])
        ]
    )

    constraintAlgorithm = ma_fields.String(validate=[OneOf(["Lincs", "Shake"])])

    electrostaticInteractions = ma_fields.Nested(
        lambda: ElectrostaticInteractionsUISchema()
    )

    fourierSpacing = ma_fields.Float()

    lincsIter = ma_fields.Integer()

    lincsOrder = ma_fields.Integer()

    neighbourList = ma_fields.Nested(lambda: NeighbourListUISchema())

    nstcomm = ma_fields.Float()

    thermostat = ma_fields.Nested(lambda: ThermostatUISchema())

    vanDerWaalsInteractions = ma_fields.Nested(
        lambda: VanDerWaalsInteractionsUISchema()
    )


class MainInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    AWHAdaptiveBiasing = ma_fields.String(validate=[OneOf(["yes", "no"])])

    boxSizeAndShape = ma_fields.Float()

    forceField = ma_fields.String()

    freeEnergyCalculation = ma_fields.String(validate=[OneOf(["yes", "no"])])

    molecules = ma_fields.List(ma_fields.Nested(lambda: MoleculesItemUISchema()))

    referencePressure = ma_fields.List(ma_fields.List(ma_fields.Float()))

    referenceTemperature = ma_fields.List(ma_fields.Float())

    simulationLength = ma_fields.Float()

    simulationTimeStep = ma_fields.Float()

    simulationType = ma_fields.String(
        validate=[
            OneOf(
                ["free energy simulation", "molecular dynamics", "energy minimization"]
            )
        ]
    )

    statisticalEnsemble = ma_fields.String(validate=[OneOf(["NpT", "NVT", "NVE"])])

    umbrellaSampling = ma_fields.String(validate=[OneOf(["yes", "no"])])


class ThermostatUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nsttcouple = ma_fields.Float()

    tauT = ma_fields.List(ma_fields.Float())

    tcGrps = ma_fields.List(ma_fields.Nested(lambda: TcGrpsItemUISchema()))

    tcoupl = ma_fields.String(
        validate=[
            OneOf(
                [
                    "no",
                    "berendsen",
                    "nose-hoover",
                    "andersen",
                    "andersen-massive",
                    "v-rescale",
                ]
            )
        ]
    )


class BarostatUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    compressibility = ma_fields.List(ma_fields.List(ma_fields.Float()))

    pcoupl = ma_fields.String(
        validate=[OneOf(["no", "Berendsen", "C-rescale", "Parrinello-Rahman", "MTTK"])]
    )

    refcoordScaling = ma_fields.String(validate=[OneOf(["no", "all", "com"])])

    tauP = ma_fields.Float()


class ElectrostaticInteractionsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coulombModifier = ma_fields.String(validate=[OneOf(["Potential-shift", "None"])])

    epsilonR = ma_fields.Float()

    epsilonRF = ma_fields.Float()

    rcoulomb = ma_fields.Float()


class MoleculesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    count = ma_fields.Integer()

    name = ma_fields.String()


class NeighbourListUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    cutoffScheme = ma_fields.String(validate=[OneOf(["Verlet", "group"])])

    nstlist = ma_fields.Float()

    pbc = ma_fields.String(validate=[OneOf(["xyz", "no", "xy"])])

    rlist = ma_fields.Float()


class RelatedFilesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    key = ma_fields.String()


class SoftwareUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    extractorVersion = ma_fields.String()

    gromacsVersion = ma_fields.String()

    tpxVersion = ma_fields.String()


class TcGrpsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    nr = ma_fields.Integer()


class TimestampsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    metadataExtractionTimestamp = LocalizedDateTime()

    tprFileTimestamp = LocalizedDateTime()


class VanDerWaalsInteractionsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dispcorr = ma_fields.String(validate=[OneOf(["No", "EnerPres", "Ener"])])

    rvdw = ma_fields.Float()

    rvdwSwitch = ma_fields.Float()

    vdwModifier = ma_fields.String(
        validate=[
            OneOf(["None", "Potential-shift", "Force-switch", "Potential-switch"])
        ]
    )
