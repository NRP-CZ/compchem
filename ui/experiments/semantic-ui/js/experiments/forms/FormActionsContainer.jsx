import React, { useState, useEffect, useRef } from 'react';
import { Paper, Grid } from '@mui/material';
import { Save, Visibility, CloudUpload, Delete } from '@mui/icons-material';
import { LoadingButton } from "@mui/lab";

import { useFormContext } from './context';
import { publishRecord } from '../util/apiClient';
import { deepEquals, validateMetadata } from '../util/metadataValidator';
import { createRecord, editRecord, uploadFileToRecord, modifyFileInRecord, deleteFileFromRecord } from '../util/apiClient';


const commitFiles = async (recordId, files, localFiles, remoteFiles, deletedFiles) => {

    const promises = files.map(async (fileName) => {
        let response = null;

        if (localFiles.hasOwnProperty(fileName) && remoteFiles.includes(fileName))
            response = await modifyFileInRecord(recordId, fileName, localFiles[fileName]);
        else if (deletedFiles.includes(fileName))
            response = await deleteFileFromRecord(recordId, fileName);
        else if (localFiles.hasOwnProperty(fileName))
            response = await uploadFileToRecord(recordId, localFiles[fileName]);
        else
            return { fileName, success: true };

        if (!response.ok)
            return { fileName, success: false };

        return { fileName, success: true };
    });

    const results = await Promise.all(promises);

    const failedFiles = results
        .filter(result => !result.success)
        .map(result => result.fileName);

    return failedFiles;
}

const updateLocalState = (failedFiles, localFiles, setLocalFiles, remoteFiles, setRemoteFiles, deletedFiles, setDeletedFiles, files) => {
    const newLocalFiles = { ...localFiles };
    const newRemoteFiles = [...remoteFiles];
    const newDeletedFiles = [...deletedFiles];

    for (const fileName of files) {
        if (failedFiles.includes(fileName))
            continue;

        if (newLocalFiles.hasOwnProperty(fileName)) {
            delete newLocalFiles[fileName];
            newRemoteFiles.push(fileName);
        } else if (newDeletedFiles.includes(fileName)) {
            newDeletedFiles.splice(newDeletedFiles.indexOf(fileName), 1);
            newRemoteFiles.splice(newRemoteFiles.indexOf(fileName), 1);
        }
    }

    setLocalFiles(newLocalFiles);
    setRemoteFiles(newRemoteFiles);
    setDeletedFiles(newDeletedFiles);
}

const getUrlParam = (name) => {
    const params = new URLSearchParams(window.location.search);
    return params.get(name);
}


const FromActionsContainer = () => {
    const { record, setRecord, localFiles, setLocalFiles, deletedFiles, setDeletedFiles, remoteFiles, setRemoteFiles, files, showDialog } = useFormContext()

    const [saved, setSaved] = useState(true);
    const [saving, setSaving] = useState(false);
    const [publishing, setPublishing] = useState(false);
    const [deleting, setDeleting] = useState(false);
    const [previewing, setPreviewing] = useState(false);

    const prevRecordRef = useRef();
    const prevFilesRef = useRef();

    useEffect(() => {
        const prevRecord = prevRecordRef.current;
        const prevFiles = prevFilesRef.current;

        if (record && prevRecord && !deepEquals(record, prevRecord))
            setSaved(false);
        else if (files && prevFiles && !deepEquals(files, prevFiles))
            setSaved(false);
        else
            return;

        prevRecordRef.current = record;
        prevFilesRef.current = files;
    }, [record, files]);


    const handleSave = async () => {
        setSaving(true);

        const errors = validateMetadata(record.metadata);
        if (errors.length > 0) {
            showDialog(
                'Validation failed',
                'There are errors in the form. Please correct them before saving.',
                () => {}
            );
            return;
        }
    
        try {
            const creatingNew = !record.id || record.id === "";
            let response = null;
    
            if (creatingNew)
                response = await createRecord(getUrlParam('community'), record.metadata);
            else
                response = await editRecord(record.id, record.metadata);

            if (!response.ok)
                throw new Error('Failed to upload metadata.');

            const newRecord = response.data;

            const failedFiles = await commitFiles(newRecord.id, files, localFiles, remoteFiles, deletedFiles);
            if (failedFiles.length > 0) {
                showDialog(
                    'Failed to save some files',
                    `These files could not be saved:\n${failedFiles.join('\n')}`,
                    () => {}
                );
                return;
            }

            setRecord(newRecord);
            updateLocalState(failedFiles, localFiles, setLocalFiles, remoteFiles, setRemoteFiles, deletedFiles, setDeletedFiles, files);

            if (creatingNew)
                window.location.href = newRecord.links.edit_html;
        } catch (error) {
            console.error('Error saving the record:', error);
            showDialog(
                'Save failed',
                'An error occurred while saving the record. Please try again.',
                () => {}
            );
        }

        console.log('Record saved');
        setSaving(false);
        setSaved(true);
    };

    const handlePreview = () => {
        setPreviewing(true);

        if (saved) {
            window.location.href = record.links.self_html;
            return;
        }

        showDialog(
            'Save changes?',
            'You have unsaved changes. Do you want to save them before leaving the page?',
            () => {
                handleSave();
                window.location.href = record.links.self_html;
            }
        )

        setPreviewing(false);
    };

    const handlePublish = async () => {
        setPublishing(true);

        showDialog(
            'Publish record?',
            'Are you sure you want to publish this record? You cannot undo this action.',
            () => {
                publishRecord(record.id);
            }
        )

        setPublishing(false);
    };

    const handleDelete = () => {
        setDeleting(true);

        // TODO
        console.log('Deleting record...');

        setDeleting(false);
    };

    return (
        <Paper elevation={3} sx={{ p: 2 }}>
            <Grid container spacing={2}>
                <Grid item xs={6} display="flex" justifyContent="center">
                    <LoadingButton loading={saving} color="primary" variant="contained" startIcon={<Save />} onClick={handleSave} sx={{ width: "128px" }}>
                        Save
                    </LoadingButton>
                </Grid>
                <Grid item xs={6} display="flex" justifyContent="center">
                    <LoadingButton loading={previewing} color="secondary" variant="contained" startIcon={<Visibility />} onClick={handlePreview} sx={{ width: "128px" }}>
                        Preview
                    </LoadingButton>
                </Grid>
                <Grid item xs={6} display="flex" justifyContent="center">
                    <LoadingButton loading={publishing} color="success" variant="contained" startIcon={<CloudUpload />} onClick={handlePublish} disabled={!saved} sx={{ width: "128px" }}>
                        Publish
                    </LoadingButton>
                </Grid>
                <Grid item xs={6} display="flex" justifyContent="center">
                    <LoadingButton loading={deleting} color="error" variant="contained" startIcon={<Delete />} onClick={handleDelete} sx={{ width: "128px" }}>
                        Delete
                    </LoadingButton>
                </Grid>
            </Grid>
        </Paper>
    );
};

export default FromActionsContainer;
