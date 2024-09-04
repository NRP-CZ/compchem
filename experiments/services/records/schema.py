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
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    validate_datetime,
    validate_identifier,
)


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class ExperimentsSchema(BaseRecordSchema):
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
        ma_fields.Nested(
            lambda: NRObjectIdentifierSchema(),
            validate=[lambda value: validate_identifier(value)],
        )
    )

    publisher = ma_fields.String()

    simulations = ma_fields.List(ma_fields.Nested(lambda: SimulationsItemSchema()))


class SimulationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _dump_sw_version = ma_fields.String()

    _gromacs_version = ma_fields.String()

    _metadata_date = ma_fields.String(validate=[validate_datetime])

    _record_file = ma_fields.String()

    _record_url = ma_fields.String()

    _tpr_date = ma_fields.String(validate=[validate_datetime])

    _tpx_version = ma_fields.String()

    _uniprot_id = ma_fields.String()

    detailed_information = ma_fields.Nested(lambda: DetailedInformationSchema())

    file_identification = ma_fields.Nested(lambda: FileIdentificationSchema())

    main_information = ma_fields.Nested(lambda: MainInformationSchema())


class DetailedInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    barostat = ma_fields.Nested(lambda: BarostatSchema())

    comm_mode = ma_fields.String(
        data_key="comm-mode",
        attribute="comm-mode",
        validate=[
            OneOf(["linear", "angular", "linear-acceleration-correction", "none"])
        ],
    )

    constraint_algorithm = ma_fields.String(
        data_key="constraint-algorithm",
        attribute="constraint-algorithm",
        validate=[OneOf(["lincs", "shake"])],
    )

    electrostatic_interactions = ma_fields.Nested(
        lambda: ElectrostaticInteractionsSchema()
    )

    fourierspacing = ma_fields.Float()

    lincs_iter = ma_fields.Integer(data_key="lincs-iter", attribute="lincs-iter")

    lincs_order = ma_fields.Integer(data_key="lincs-order", attribute="lincs-order")

    neighbour_list = ma_fields.Nested(lambda: NeighbourListSchema())

    nstcomm = ma_fields.Integer()

    thermostat = ma_fields.Nested(lambda: ThermostatSchema())

    van_der_Waals_interactions = ma_fields.Nested(
        lambda: VanDerWaalsInteractionsSchema()
    )


class MainInformationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    AWH_adaptive_biasing = ma_fields.Boolean()

    box_size_and_shape = ma_fields.Float()

    force_field = ma_fields.String()

    free_energy_calculation = ma_fields.String(validate=[OneOf([True, False])])

    molecules = ma_fields.List(ma_fields.Nested(lambda: MoleculesItemSchema()))

    reference_pressure = ma_fields.List(
        ma_fields.List(ma_fields.List(ma_fields.Float()))
    )

    reference_temperature = ma_fields.List(ma_fields.Float())

    simulation_length = ma_fields.Float()

    simulation_time_step = ma_fields.Float()

    simulation_type = ma_fields.String(
        validate=[
            OneOf(
                ["free energy simulation", "molecular dynamics", "energy minimization"]
            )
        ]
    )

    statistical_ensamble = ma_fields.String(
        validate=[
            OneOf(
                ["NVE (microcanonical)", "NVT (canonical)", "NpT (isothermal-isobaric)"]
            )
        ]
    )

    umbrella_sampling = ma_fields.Boolean()


class ThermostatSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nsttcouple = ma_fields.Integer()

    tau_t = ma_fields.List(ma_fields.Float(), data_key="tau-t", attribute="tau-t")

    tc_grps = ma_fields.Nested(
        lambda: TcGrpsSchema(), data_key="tc-grps", attribute="tc-grps"
    )

    tcoupl = ma_fields.String(
        validate=[
            OneOf(
                [
                    False,
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
        validate=[OneOf([False, "berendsen", "c-rescale", "parrinello-rahman", "mttk"])]
    )

    refcoord_scaling = ma_fields.String(
        data_key="refcoord-scaling",
        attribute="refcoord-scaling",
        validate=[OneOf([False, "all", "com"])],
    )

    tau_p = ma_fields.Float(data_key="tau-p", attribute="tau-p")


class ElectrostaticInteractionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coulomb_modifier = ma_fields.String(
        data_key="coulomb-modifier",
        attribute="coulomb-modifier",
        validate=[OneOf(["potential-shift", "none"])],
    )

    epsilon_r = ma_fields.Float(data_key="epsilon-r", attribute="epsilon-r")

    epsilon_rf = ma_fields.Float(data_key="epsilon-rf", attribute="epsilon-rf")

    rcoulomb = ma_fields.Float()


class FileIdentificationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    doi = ma_fields.String()

    name = ma_fields.String()

    related_files = ma_fields.List(ma_fields.String())

    simulation_year = ma_fields.String()


class MoleculesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    count = ma_fields.Integer()

    name = ma_fields.String()


class NeighbourListSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    cutoff_scheme = ma_fields.String(
        data_key="cutoff-scheme",
        attribute="cutoff-scheme",
        validate=[OneOf(["verlet", "group"])],
    )

    nstlist = ma_fields.Integer()

    pbc = ma_fields.String(validate=[OneOf(["xyz", False, "xy"])])

    rlist = ma_fields.Float()


class TcGrpsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    nr = ma_fields.Integer()


class VanDerWaalsInteractionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dispcorr = ma_fields.String(validate=[OneOf([False, "enerpres", "eber"])])

    rvdw = ma_fields.Float()

    rvdw_switch = ma_fields.Float(data_key="rvdw-switch", attribute="rvdw-switch")

    vdw_modifier = ma_fields.String(
        data_key="vdw-modifier",
        attribute="vdw-modifier",
        validate=[
            OneOf(["potential-shift", "none", "force-switch", "potential-switch"])
        ],
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
