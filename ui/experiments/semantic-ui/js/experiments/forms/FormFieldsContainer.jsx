import React, { useState, useEffect } from 'react'
import { Stack } from "@mui/material";

import Dropzone from "./components/Dropzone"
import SimulationEditor from "./components/SimulationEditor"
import ExperimentEditor from './components/ExperimentEditor'
import { validateMetadata } from '../util/metadataValidator'
import { useFormContext } from './context'


const FormFieldsContainer = () => {
    const { record, setRecord, files, setFiles } = useFormContext()
    const [data, setData] = useState(record.metadata || {})
    const [simulations, setSimulations] = useState(data.simulations || [])


    useEffect(() => {
        setRecord(prevRecord => ({
            ...prevRecord,
            metadata: data
        }));
    }, [data]);

    useEffect(() => {
        setData(prevData => ({
            ...prevData,
            simulations: simulations
        }));
    }, [simulations]);


    return (
        <Stack spacing={5}>
            <ExperimentEditor
                data={data}
                setData={setData}
            />

            <Dropzone
                setSimulations={setSimulations}
            />

            <SimulationEditor
                simulations={simulations}
                setSimulations={setSimulations}
            />

            {/*
            <h1>DEBUG: Metadata</h1>
            <button onClick={() => console.log(validateMetadata(data))}>Validate</button>
            <pre>
                {JSON.stringify(record, null, 4)}
            </pre>
            */}
        </Stack>
    )
}

export default FormFieldsContainer
