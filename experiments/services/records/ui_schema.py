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

    _dump_sw_version = ma_fields.String()

    _gromacs_version = ma_fields.String()

    _metadata_date = LocalizedDateTime()

    _record_file = ma_fields.String()

    _record_url = ma_fields.String()

    _tpr_date = LocalizedDateTime()

    _tpx_version = ma_fields.String()

    _uniprot_id = ma_fields.String()

    detailed_information = ma_fields.Nested(lambda: DetailedInformationUISchema())

    file_identification = ma_fields.Nested(lambda: FileIdentificationUISchema())

    main_information = ma_fields.Nested(lambda: MainInformationUISchema())


class DetailedInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    barostat = ma_fields.Nested(lambda: BarostatUISchema())

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
        lambda: ElectrostaticInteractionsUISchema()
    )

    fourierspacing = ma_fields.Float()

    lincs_iter = ma_fields.Integer(data_key="lincs-iter", attribute="lincs-iter")

    lincs_order = ma_fields.Integer(data_key="lincs-order", attribute="lincs-order")

    neighbour_list = ma_fields.Nested(lambda: NeighbourListUISchema())

    nstcomm = ma_fields.Integer()

    thermostat = ma_fields.Nested(lambda: ThermostatUISchema())

    van_der_Waals_interactions = ma_fields.Nested(
        lambda: VanDerWaalsInteractionsUISchema()
    )


class MainInformationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    AWH_adaptive_biasing = ma_fields.Boolean()

    box_size_and_shape = ma_fields.Float()

    force_field = ma_fields.String()

    free_energy_calculation = ma_fields.String(validate=[OneOf([True, False])])

    molecules = ma_fields.List(ma_fields.Nested(lambda: MoleculesItemUISchema()))

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


class ThermostatUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nsttcouple = ma_fields.Integer()

    tau_t = ma_fields.List(ma_fields.Float(), data_key="tau-t", attribute="tau-t")

    tc_grps = ma_fields.Nested(
        lambda: TcGrpsUISchema(), data_key="tc-grps", attribute="tc-grps"
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


class BarostatUISchema(DictOnlySchema):
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


class ElectrostaticInteractionsUISchema(DictOnlySchema):
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


class FileIdentificationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authors = ma_fields.List(ma_fields.String())

    description = ma_fields.String()

    doi = ma_fields.String()

    name = ma_fields.String()

    related_files = ma_fields.List(ma_fields.String())

    simulation_year = ma_fields.String()


class MoleculesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    count = ma_fields.Integer()

    name = ma_fields.String()


class NeighbourListUISchema(DictOnlySchema):
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


class TcGrpsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    nr = ma_fields.Integer()


class VanDerWaalsInteractionsUISchema(DictOnlySchema):
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
