import React, { useEffect, useState } from "react";
import { CheckCircle, Error, Delete, SettingsRounded } from "@mui/icons-material";
import { Grid, IconButton, Stack, Typography } from "@mui/material";

import schema from "../schemas/gmx-schema.json"
import uischema from "../schemas/gmx-uischema.json"
import theme from "../theme"

import FormsWrapper from "./FormsWrapper"
import { validateSimulation } from "../../util/metadataValidator";
import { useFormContext } from "../context";


const ITEM_PREFIX = "analyze-";


const updateIndex = (prev, index, value) => {
    const newData = [...prev];
    newData[index] = value;
    return newData;
}

const deleteIndex = (prev, index) => {
    const newData = [...prev];
    newData.splice(index, 1);
    return newData;
}


const SimulationEditor = ({ simulations, setSimulations }) => {
    const { files, deletedFiles, showDialog } = useFormContext();

    const [simulationSchema, setSimulationSchema] = useState(schema);
    const [editingSimulationIdx, setEditingSimulationIdx] = useState(null);


    useEffect(() => {
        const newSchema = {...simulationSchema};
        const validFiles = files.filter(filename => !deletedFiles.includes(filename));
        const tprFiles = validFiles.filter(fileName => fileName.endsWith('.tpr'));

        newSchema.properties.file_identification.properties.name.enum = tprFiles.length > 0 ? tprFiles : [""];
        newSchema.properties.file_identification.properties.related_files.items.enum = validFiles.length > 0 ? validFiles : [""];
        setSimulationSchema(newSchema);
    }, [files]);

    useEffect(() => {
        for (let i = 0; i < simulations.length; i++) {
            const obj = document.getElementById(ITEM_PREFIX + i);
            obj.style.backgroundColor = "white";
            obj.style.color = "black";
        }

        if (editingSimulationIdx != null) {
            const obj = document.getElementById(ITEM_PREFIX + editingSimulationIdx);
            obj.style.backgroundColor = theme.palette.primary.main;
            obj.style.color = "white";
        }
    }, [editingSimulationIdx])


    const editSimulation = (idx) => {
        setEditingSimulationIdx(prev => (prev === idx) ? null : idx)
    }

    const deleteSimulation = (idx) => {
        showDialog(
            'Delete simulation?',
            'Are you sure you want to delete this simulation?',
            () => {
                setSimulations((prev) => deleteIndex(prev, idx));
    
                if (editingSimulationIdx === null)
                    return;
                if (editingSimulationIdx === idx)
                    setEditingSimulationIdx(null);
                else if (editingSimulationIdx > idx)
                    setEditingSimulationIdx(prev => prev - 1);
            }
        )
    }

    return (
        <Stack direction="column" spacing={5}>

            {simulations.length > 0 && (
                <>
                    <Typography variant="h3">Simulation metadata</Typography>
                    <Typography variant="h4">Select simulation</Typography>
                    <Stack direction="column" spacing={1} justifyItems={"center"}>
                        {simulations.map((simulation, idx) => (
                            <Grid container key={idx} id={ITEM_PREFIX + idx} onClick={() => editSimulation(idx)} alignItems={"center"} sx={{ border: '1px solid', borderColor: 'grey.300', borderRadius: 1, p: 1 }}>
                                <Grid item xs={1}>
                                    {validateSimulation(simulation, idx).length === 0 && (
                                        <CheckCircle color="success" sx={{ fontSize: "3em" }} />
                                    ) || (
                                        <Error color="error" sx={{ fontSize: "3em" }} />
                                    )}
                                </Grid>
                                <Grid item xs={10}>
                                    <Typography variant="h6">Simulation {idx+1}</Typography>
                                </Grid>
                                <Grid item xs={1} container justifyContent="flex-end">
                                    <IconButton onClick={(e) => { e.stopPropagation(); deleteSimulation(idx); }}><Delete color="error" /></IconButton>
                                </Grid>
                            </Grid>
                        ))}
                    </Stack>
                </>
            )}

            {editingSimulationIdx != null && (
                <FormsWrapper
                    schema={simulationSchema}
                    uischema={uischema}
                    data={simulations[editingSimulationIdx]}
                    setData={(data) => setSimulations((prev) => updateIndex(prev, editingSimulationIdx, data))}
                />
            )}
        </Stack>
    );
}

export default SimulationEditor;
