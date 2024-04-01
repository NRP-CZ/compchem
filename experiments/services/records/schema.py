import marshmallow as ma
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.utils import get_value
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode
from nr_metadata.common.services.records.schema_datatypes import (
    NRCreatorSchema,
    NRFundingReferenceSchema,
)
from nr_metadata.schema.identifiers import NRObjectIdentifierSchema
from oarepo_requests.services.schema import RequestsSchemaMixin
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import validate_datetime


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class ExperimentsSchema(RequestsSchemaMixin, BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: ExperimentsMetadataSchema())
    parent = ma.fields.Nested(GeneratedParentSchema)
    files = ma.fields.Nested(
        lambda: FilesOptionsSchema(), load_default={"enabled": True}
    )

    # todo this needs to be generated for [default preview] to work
    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        if attr == "files":
            return getattr(obj, attr, default)
        else:
            return get_value(obj, attr, default)


class ExperimentsMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    creators = ma_fields.List(ma_fields.Nested(lambda: NRCreatorSchema()))

    description = ma_fields.String()

    fundingReference = ma_fields.Nested(lambda: NRFundingReferenceSchema())

    name = ma_fields.String()

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierSchema())
    )

    publisher = ma_fields.String()

    simulations = ma_fields.List(ma_fields.Nested(lambda: SimulationsItemSchema()))


class SimulationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    detailedInformation = ma_fields.Nested(lambda: DetailedInformationSchema())

    key = ma_fields.String()

    mainInformation = ma_fields.Nested(lambda: MainInformationSchema())

    relatedFiles = ma_fields.List(ma_fields.Nested(lambda: RelatedFilesItemSchema()))

    simulationYear = ma_fields.Integer()

    software = ma_fields.Nested(lambda: SoftwareSchema())

    timestamps = ma_fields.Nested(lambda: TimestampsSchema())


class DetailedInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    barostat = ma_fields.Nested(lambda: BarostatSchema())

    commMode = ma_fields.String(
        validate=[
            OneOf(["Linear", "Angular", "Linear-acceleration-correction", "None"])
        ]
    )

    constraintAlgorithm = ma_fields.String(validate=[OneOf(["Lincs", "Shake"])])

    electrostaticInteractions = ma_fields.Nested(
        lambda: ElectrostaticInteractionsSchema()
    )

    fourierSpacing = ma_fields.Float()

    lincsIter = ma_fields.Integer()

    lincsOrder = ma_fields.Integer()

    neighbourList = ma_fields.Nested(lambda: NeighbourListSchema())

    nstcomm = ma_fields.Float()

    thermostat = ma_fields.Nested(lambda: ThermostatSchema())

    vanDerWaalsInteractions = ma_fields.Nested(lambda: VanDerWaalsInteractionsSchema())


class MainInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    AWHAdaptiveBiasing = ma_fields.String(validate=[OneOf(["yes", "no"])])

    boxSizeAndShape = ma_fields.Float()

    forceField = ma_fields.String()

    freeEnergyCalculation = ma_fields.String(validate=[OneOf(["yes", "no"])])

    molecules = ma_fields.List(ma_fields.Nested(lambda: MoleculesItemSchema()))

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


class ThermostatSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nsttcouple = ma_fields.Float()

    tauT = ma_fields.List(ma_fields.Float())

    tcGrps = ma_fields.List(ma_fields.Nested(lambda: TcGrpsItemSchema()))

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


class BarostatSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    compressibility = ma_fields.List(ma_fields.List(ma_fields.Float()))

    pcoupl = ma_fields.String(
        validate=[OneOf(["no", "Berendsen", "C-rescale", "Parrinello-Rahman", "MTTK"])]
    )

    refcoordScaling = ma_fields.String(validate=[OneOf(["no", "all", "com"])])

    tauP = ma_fields.Float()


class ElectrostaticInteractionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coulombModifier = ma_fields.String(validate=[OneOf(["Potential-shift", "None"])])

    epsilonR = ma_fields.Float()

    epsilonRF = ma_fields.Float()

    rcoulomb = ma_fields.Float()


class MoleculesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    count = ma_fields.Integer()

    name = ma_fields.String()


class NeighbourListSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    cutoffScheme = ma_fields.String(validate=[OneOf(["Verlet", "group"])])

    nstlist = ma_fields.Float()

    pbc = ma_fields.String(validate=[OneOf(["xyz", "no", "xy"])])

    rlist = ma_fields.Float()


class RelatedFilesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    key = ma_fields.String()


class SoftwareSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    extractorVersion = ma_fields.String()

    gromacsVersion = ma_fields.String()

    tpxVersion = ma_fields.String()


class TcGrpsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    nr = ma_fields.Integer()


class TimestampsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    metadataExtractionTimestamp = ma_fields.String(validate=[validate_datetime])

    tprFileTimestamp = ma_fields.String(validate=[validate_datetime])


class VanDerWaalsInteractionsSchema(DictOnlySchema):
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


class FilesOptionsSchema(ma.Schema):
    """Basic files options schema class."""

    enabled = ma.fields.Bool(missing=True)
    # allow unsetting
    default_preview = SanitizedUnicode(allow_none=True)

    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        value = getattr(obj, attr, default)

        if attr == "default_preview" and not value:
            return default

        return value
