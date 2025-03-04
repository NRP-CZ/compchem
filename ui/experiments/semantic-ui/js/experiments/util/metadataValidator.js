import { validate } from '@jsonforms/core';
import Ajv from 'ajv';

import experiment_schema from "../forms/schemas/gmx-schema.json"
import gmx_schema from "../forms/schemas/gmx-schema.json"


const ajv = new Ajv({allErrors: true})
const experimentValidator = ajv.compile(experiment_schema)
const gmxValidator = ajv.compile(gmx_schema)


export const validateMetadata = (metadata) => {
    // Validate the top-level experiment metadata
    let errors = validate(experimentValidator, metadata)

    // Validate each simulation
    const simulations = metadata.simulations

    simulations.forEach((simulation, index) => {
        const simulationErrors = validateSimulation(simulation, index)
        errors = errors.concat(simulationErrors)
    })

    return errors;
}


export const validateSimulation = (simulation, index) => {
    let errors = []
    const gmxErrors = validate(gmxValidator, simulation)

    gmxErrors.forEach((error) => {
        error.instancePath = `simulations[${index}]${error.instancePath}`
        errors.push(error)
    })

    return errors;
}


export const deepEquals = (a, b) => {
    return JSON.stringify(a) === JSON.stringify(b)
}
