import React, { useEffect, useState } from "react";
import { useDropzone } from "react-dropzone";
import { parse } from 'yaml'
import { Check, FileUpload, RemoveCircle } from "@mui/icons-material";
import { Box, Grid, IconButton, Paper, Stack, Typography } from "@mui/material";
import { LoadingButton } from "@mui/lab";

const Dropzone = ({fileMetadata, setFileMetadata}) => {
    const {
        getRootProps,
        getInputProps
    } = useDropzone({
        accept: ['.tpr', '.json', '.yaml'],
        onDrop: (acceptedFiles) => setAcceptedFiles(acceptedFiles)
    });

    const [acceptedFiles, setAcceptedFiles] = useState([]);     // list of file objects
    const [uploaded, setUploaded] = useState(false);
    const [analyzing, setAnalyzing] = useState({});             // {filename: bool}
    let pdbData = null;

    useEffect(() => {
        if (acceptedFiles.length > 0) {
            setUploaded(true);
        } else {
            setUploaded(false);
        }
    }, [acceptedFiles]);

    const clearFile = (index) => {
        const newAcceptedFiles = [...acceptedFiles];
        const fileName = newAcceptedFiles[index].name;
        newAcceptedFiles.splice(index, 1);

        const newAnalyzing = {...analyzing};
        delete newAnalyzing[fileName];

        if (newAcceptedFiles.length === 0) {
            setUploaded(false);
        }

        setAcceptedFiles(newAcceptedFiles);
        setAnalyzing(newAnalyzing);
    };

    const analyzeTPR = async(file) => {
        const fileName = file.name;
        setAnalyzing((prev) => ({ ...prev, [fileName]: true }));
        let requestData = new FormData();
        requestData.append('file', file);

        const getMetadata = fetch('https://gmxmetadump.biodata.ceitec.cz/api/analyze', { body: requestData, method: 'POST' })
            .then(response => response.text())
            .then(text => text.replace('Infinity', '-1'))
            .then(text => JSON.parse(text));
        const getPdb = fetch('https://gmxmetadump.biodata.ceitec.cz/api/get_pdb', { body: requestData, method: 'POST' })
            .then(response => response.blob())
            .then(blob => blob.text());

        // TODO: upload file to server (how to handle JSON/YAML ?)

        let [metadata, pdbString] = await Promise.all([getMetadata, getPdb]);
        pdbData = pdbString;
        setAnalyzing((prev) => ({ ...prev, [fileName]: false }));
        return metadata;
    };

    const extractMetadata = async (file) => {
        const extension = file.name.split('.').pop();
        let data;

        try {
            switch (extension) {
                case "tpr":
                    data = await analyzeTPR(file);
                    break;
                case "json":
                    data = JSON.parse(await file.text());
                    break;
                case "yaml":
                case "yml":
                    data = parse(await file.text());
                    break;
                default:
                    throw new Error('Invalid file type.');
            }
        } catch (error) {
            console.error(error);
            return;
        }

        const defaultData = {
            file_identification: {},
            main_information: {},
            detailed_information: {}
        };

        const metadata = {...defaultData, ...data};
        console.log(metadata);

        setFileMetadata((prev) => ({...prev, [file.name]: metadata}));
    };

    return (
        <Stack direction="column" spacing={5}>
            <Typography variant="h2">Upload Files</Typography>
            <Box>
                <Stack direction="column" spacing={1}>
                    <Paper elevation={0} sx={{ p: 5, textAlign: "center", border: "2.5px dashed", "&:hover": { borderColor: "#008691", cursor: "pointer" } }} variant="outlined" >
                        <div {...getRootProps({ className: 'dropzone' })}>
                            <input {...getInputProps()} />
                            <FileUpload sx={{ fontSize: "7em", color: "#008691" }} />
                            <Typography variant="h3">Upload files here</Typography>
                            <Typography variant="subtitle1"><em>(Only [*.tpr *.json *.yaml] are accepted)</em></Typography>
                        </div>
                    </Paper>

                    {uploaded && (
                        <Stack direction="column" spacing={1} justifyItems={"center"} sx={{ p: 2 }}>
                            <Typography variant="h4">Files chosen</Typography>
                            {acceptedFiles.map((file, index) => (
                                <Grid
                                    container
                                    key={file.name}
                                    alignItems={"center"}
                                    sx={{
                                        border: '1px solid',
                                        borderColor: 'grey.300',
                                        borderRadius: 1
                                    }}
                                >
                                    <Grid item xs={2} sx={{ textAlign: "center", p: "0.8em", borderRadius: "50%" }}>
                                        <Check sx={{ fontSize: "3em", color: "#007d00a1" }} />
                                    </Grid>
                                    <Grid item xs={7}>
                                        <Typography variant="h5">{file.name}</Typography>
                                    </Grid>
                                    <Grid item xs={3} justifyItems={"center"} justifyContent={"space-evenly"} direction={"row"}>
                                        <LoadingButton loading={analyzing[file.name]} variant="contained" size="large" color="primary" disabled={!uploaded} onClick={async () => {await extractMetadata(file); clearFile(index)}}>Analyze</LoadingButton>
                                        <IconButton color="error" size="large" onClick={() => clearFile(index)}><RemoveCircle /></IconButton>
                                    </Grid>
                                </Grid>
                            ))}
                        </Stack>
                    )}
                </Stack>
            </Box>
        </Stack>
    );
}

export default Dropzone;
