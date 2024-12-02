import React, { useEffect, useState } from "react";
import { CloudDone, Check, FileUpload, RemoveCircle } from "@mui/icons-material";
import { Box, Button, Grid, IconButton, Paper, Stack, Typography } from "@mui/material";

import FormsWrapper from "./FormsWrapper"

const FileMetadataEditor = ({fileMetadata, setFileMetadata, fileErrors, setFileErrors}) => {
    const [editingFileName, setEditingFileName] = useState(null);
    // const [formErrors, setFormErrors] = useState(undefined);
    // TODO: convert errors to a dict for checking errors before saving record

    const editFile = (fileName) => {
        const prefix = "analyze-"

        // disable editing (hides the form component)
        if (editingFileName === fileName) {
            setEditingFileName(null);
            document.getElementById(prefix + fileName).style.backgroundColor = "white";
            document.getElementById(prefix + fileName).style.color = "black";
            return;
        }

        // reset colors of other files
        Object.keys(fileMetadata).forEach((fileName) => {
            const obj = document.getElementById(prefix + fileName);
            if (obj) {
                obj.style.backgroundColor = "white";
                obj.style.color = "black";
            }
        });

        const obj = document.getElementById(prefix + fileName);
        obj.style.backgroundColor = "#008691";
        obj.style.color = "white";

        setEditingFileName(fileName);
    }

    const deleteFile = (fileName) => {
        // TODO
        console.log("[TODO] deleting", fileName);
    }

    return (
        <Stack direction="column" spacing={5}>
            {Object.keys(fileMetadata).length > 0 && (
                <Typography variant="h2">Edit Metadata</Typography>
            )}

            {Object.keys(fileMetadata).length > 0 && (
                <Stack direction="column" spacing={1} justifyItems={"center"} sx={{ p: 2, mt: 2 }}>
                    <Typography variant="h4">Files to analyze</Typography>
                    {Object.keys(fileMetadata).map((fileName) => (
                        <Grid
                            container
                            key={fileName}
                            id={"analyze-" + fileName}
                            onClick={() => editFile(fileName)}
                            alignItems={"center"}
                            sx={{
                                border: '1px solid',
                                borderColor: 'grey.300',
                                borderRadius: 1
                            }}
                        >
                            <Grid item xs={2} sx={{ textAlign: "center", p: "0.8em", borderRadius: "50%" }}>
                                <CloudDone sx={{ fontSize: "3em", color: "#007d00a1" }} />
                            </Grid>
                            <Grid item xs={9}>
                                <Typography variant="h6">{fileName}</Typography>
                            </Grid>
                            <Grid item xs={1} justifyItems={"center"} justifyContent={"space-evenly"} direction={"row"}>
                                <IconButton color="error" size="large" onClick={() => deleteFile(fileName)}><RemoveCircle /></IconButton>
                            </Grid>
                        </Grid>
                    ))}
                </Stack>
            )}

            {editingFileName != null && (
                <FormsWrapper
                    data={fileMetadata[editingFileName]}
                    setData={(data) => setFileMetadata((prev) => ({...prev, [editingFileName]: data}))}
                    errors={fileErrors[editingFileName]}
                    setErrors={(errors) => setFileErrors((prev) => ({...prev, [editingFileName]: errors}))}
                />
            )}
        </Stack>
    );
}

export default FileMetadataEditor;
