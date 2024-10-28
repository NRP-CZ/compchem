import marshmallow as ma
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
from oarepo_communities.schemas.parent import CommunitiesParentSchema
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    validate_datetime,
    validate_identifier,
)
from oarepo_workflows.services.records.schema import WorkflowParentSchema


class GeneratedParentSchema(WorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)

    communities = ma_fields.Nested(CommunitiesParentSchema)


class ExperimentsSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: ExperimentsMetadataSchema())

    state = ma_fields.String(dump_only=True)
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

    version = ma_fields.String()


class SimulationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _dump_sw_version = ma_fields.String()

    _exit_code = ma_fields.Integer()

    _gromacs_version = ma_fields.String()

    _metadata_date = ma_fields.String(validate=[validate_datetime])

    _metadump_version = ma_fields.String()

    _protein_sequences = ma_fields.List(ma_fields.String())

    _record_file = ma_fields.String()

    _record_url = ma_fields.String()

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
        validate=[
            OneOf(["none", "linear", "angular", "linear-acceleration-correction"])
        ]
    )

    constraint_algorithm = ma_fields.String(validate=[OneOf(["lincs", "shake"])])

    electrostatic_interactions = ma_fields.Nested(
        lambda: ElectrostaticInteractionsSchema()
    )

    fourierspacing = ma_fields.Float()

    lincs_iter = ma_fields.Integer()

    lincs_order = ma_fields.Integer()

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

    free_energy_calculation = ma_fields.String(validate=[OneOf(["no", "yes"])])

    molecules = ma_fields.List(ma_fields.Nested(lambda: MoleculesItemSchema()))

    reference_pressure = ma_fields.List(ma_fields.List(ma_fields.Float()))

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

    tau_t = ma_fields.List(ma_fields.Float())

    tc_grps = ma_fields.Nested(lambda: TcGrpsSchema())

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
        validate=[OneOf(["no", "berendsen", "c-rescale", "parrinello-rahman", "mttk"])]
    )

    pcoupltype = ma_fields.String(
        validate=[
            OneOf(["isotropic", "semiisotropic", "anisotropic", "surface-tension"])
        ]
    )

    refcoord_scaling = ma_fields.String(validate=[OneOf(["no", "all", "com"])])

    tau_p = ma_fields.Float()


class ElectrostaticInteractionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    coulomb_modifier = ma_fields.String(validate=[OneOf(["none", "potential-shift"])])

    coulombtype = ma_fields.String(
        validate=[
            OneOf(
                [
                    "cut-off",
                    "ewald",
                    "pme",
                    "p3m-ad",
                    "reaction-field",
                    "user",
                    "pme-shift",
                    "pme-user",
                    "pme-user-switch",
                ]
            )
        ]
    )

    epsilon_r = ma_fields.Float()

    epsilon_rf = ma_fields.Float()

    rcoulomb = ma_fields.Float()


class FileIdentificationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    doi = ma_fields.String()

    name = ma_fields.String()

    related_files = ma_fields.String()

    simulation_year = ma_fields.String()


class MoleculesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    count = ma_fields.Integer()

    name = ma_fields.String()

    residues = ma_fields.List(ma_fields.String())


class NeighbourListSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    cutoff_scheme = ma_fields.String(validate=[OneOf(["verlet", "group"])])

    nstlist = ma_fields.Integer()

    pbc = ma_fields.String(validate=[OneOf(["no", "xy", "xyz"])])

    rlist = ma_fields.Float()


class TcGrpsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    nr = ma_fields.Integer()


class VanDerWaalsInteractionsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dispcorr = ma_fields.String(validate=[OneOf(["no", "enerpres", "eber"])])

    rvdw = ma_fields.Float()

    rvdw_switch = ma_fields.Float()

    vdw_modifier = ma_fields.String(
        validate=[
            OneOf(["potential-shift", "none", "force-switch", "potential-switch"])
        ]
    )

    vdw_type = ma_fields.String(
        validate=[OneOf(["cut-off", "pme", "shift", "switch", "user"])]
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
