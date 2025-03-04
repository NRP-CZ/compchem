import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { parse } from 'yaml'
import { ChangeCircle, AddCircle, RemoveCircle, Delete, Cloud, Restore, FileUpload } from "@mui/icons-material";
import { Grid, IconButton, Paper, Stack, Typography } from "@mui/material";
import { LoadingButton } from "@mui/lab";

import { useFormContext } from "../context";
import { downloadFileFromRecord } from "../../util/apiClient";

const isFileType = (fileName, ...suffixes) => {
    const extension = fileName.split('.').pop();
    return suffixes.includes(extension);
}

const Dropzone = ({ setSimulations }) => {

    const { record, files, remoteFiles, localFiles, setLocalFiles, deletedFiles, setDeletedFiles, simulationFiles, showDialog } = useFormContext();

    const {
        getRootProps,
        getInputProps
    } = useDropzone({
        accept: ['.tpr', '.json', '.yaml', '.mdb', '.gro', '.pdb', '.xtc', '.ipynb'],
        onDrop: (acceptedFiles) => { acceptedFiles.forEach((file) => { addFile(file) }) },
    })

    const analyzedFiles = Object.fromEntries(files.map(fileName => [fileName, false]));
    const [analyzing, setAnalyzing] = useState(analyzedFiles);  // {filename: bool}


    const addFile = (fileBlob) => {
        const fileName = fileBlob.name;

        // if file is already deleted, restore it
        if (deletedFiles.includes(fileName));
            restoreFile(fileName);

        setLocalFiles((prev) => ({ ...prev, [fileName]: fileBlob }));
        setAnalyzing((prev) => ({ ...prev, [fileName]: false }));
    }

    const clearFile = (fileName) => {
        if (simulationFiles.includes(fileName)) {
            let confirmed = false;

            showDialog(
                'File related to simulation',
                'This file is related to a simulation. Are you sure you want to delete it?',
                () => { confirmed = true; }
            )

            if (!confirmed)
                return;
        }

        // if file is only remote, add it to deletedFiles
        if (remoteFiles.includes(fileName) && !localFiles.hasOwnProperty(fileName)) {
            setDeletedFiles((prev) => [...prev, fileName]);
            return;
        }

        const newLocalFiles = {...localFiles};
        delete newLocalFiles[fileName];
        setLocalFiles(newLocalFiles);
    };

    const restoreFile = (fileName) => {
        const newDeletedFiles = [...deletedFiles];
        newDeletedFiles.splice(newDeletedFiles.indexOf(fileName), 1);
        setDeletedFiles(newDeletedFiles);
    }

    const analyzeTPR = async (file) => {
        const requestData = new FormData();
        requestData.append('file', file);

        const response = await fetch('https://gmxmetadump.biodata.ceitec.cz/api/analyze', {
            method: 'POST',
            body: requestData,
        });

        let text = await response.text();
        text = text.replace('Infinity', '-1');
        const metadata = JSON.parse(text);

        if (!metadata.file_identification)
            metadata.file_identification = {};

        metadata.file_identification.name = file.name;

        return metadata;
    };

    const extractMetadata = async (fileName) => {
        setAnalyzing((prev) => ({ ...prev, [fileName]: true }));

        let data;
        let file;

        if (!localFiles.hasOwnProperty(fileName)) {
            console.log("fetching file from remote");
            file = await downloadFileFromRecord(record.id, fileName, true);
        } else {
            file = localFiles[fileName];
        }

        if (isFileType(fileName, 'tpr'))
            data = await analyzeTPR(file);
        else if (isFileType(fileName, 'json'))
            data = JSON.parse(await file.text());
        else if (isFileType(fileName, 'yaml', 'yml'))
            data = parse(await file.text());

        const defaultData = {
            file_identification: {},
            main_information: {},
            detailed_information: {}
        };

        const metadata = {...defaultData, ...data};
        console.log(metadata);

        // we don't want to keep the metadata files
        if (isFileType(fileName, 'json', 'yaml', 'yml'))
            clearFile(fileName);

        setSimulations((prev) => ([...prev, metadata]));
        setAnalyzing((prev) => ({ ...prev, [fileName]: false }));
    };

    return (
        <Stack direction="column" spacing={2}>
            <Typography variant="h3">Experiment files</Typography>
            <Paper elevation={0} sx={{ p: 5, textAlign: "center", border: "2.5px dashed", "&:hover": { borderColor: "primary", cursor: "pointer" } }} variant="outlined" >
                <div {...getRootProps({ className: 'dropzone' })}>
                    <input {...getInputProps()} />
                    <FileUpload color="primary" sx={{ fontSize: "7em" }} />
                    <Typography variant="h3">Upload files here</Typography>
                    <Typography variant="subtitle1"><em>(Only [*.tpr *.json *.yaml *.mdb, *.gro, *.pdb, *.xtc, *.ipynb] are accepted)</em></Typography>
                </div>
            </Paper>

            {files.length > 0 && (
                <Stack direction="column" spacing={1} justifyItems={"center"} sx={{ p: 2 }}>
                    <Typography variant="h4">Uploaded files</Typography>
                    {files.map((fileName) => (
                        <Grid container key={fileName} alignItems={"center"} sx={{border: '1px solid', borderColor: 'grey.300', borderRadius: 1, p: 1}}>
                            <Grid item xs={1}>
                                {localFiles.hasOwnProperty(fileName) && remoteFiles.includes(fileName) && (
                                    <ChangeCircle color="warning" sx={{ fontSize: "3em" }} />
                                ) || deletedFiles.includes(fileName) && (
                                    <RemoveCircle color="error" sx={{ fontSize: "3em" }} />
                                ) || localFiles.hasOwnProperty(fileName) && (
                                    <AddCircle color="success" sx={{ fontSize: "3em" }} />
                                ) || (
                                    <Cloud color="info" sx={{ fontSize: "3em" }} />
                                )}
                            </Grid>
                            <Grid item xs={7}>
                                <Typography variant="h5">{fileName}</Typography>
                            </Grid>
                            <Grid item xs={4} container justifyContent="flex-end">
                                {isFileType(fileName, 'tpr', 'json', 'yaml', 'yml') && !simulationFiles.includes(fileName) && !deletedFiles.includes(fileName) && (
                                    <LoadingButton loading={analyzing[fileName]} variant="contained" color="primary" onClick={async () => await extractMetadata(fileName)}>Create simulation</LoadingButton>
                                )}
                                {deletedFiles.includes(fileName) && (
                                    <IconButton onClick={() => restoreFile(fileName)}><Restore color="info" /></IconButton>
                                ) || (
                                    <IconButton disabled={analyzing[fileName]} onClick={() => clearFile(fileName)}><Delete color="error" /></IconButton>
                                )}
                            </Grid>
                        </Grid>
                    ))}
                </Stack>
            )}
        </Stack>
    );
}

export default Dropzone;
