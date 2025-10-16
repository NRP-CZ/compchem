import React, { useState } from 'react';
import {
    Typography,
    Button,
    Checkbox,
    FormControlLabel,
    Divider,
    Chip,
    Stack
} from '@mui/material';
import {
    ArrowBack,
    PlayArrow,
    Description
} from '@mui/icons-material';
import { createWorkflow } from '../../util/workflowsClient';

const handleBackToWorkflows = (onBack) => () => {
    onBack();
};

const handleFileToggle = (remoteFiles, setSelectedFiles) =>
    (fileKey) => {
        const fileObject = remoteFiles.find(file => file.key === fileKey);
        if (!fileObject) return;

        setSelectedFiles(prev => {
            const isSelected = prev.some(f => f.key === fileKey);
            if (isSelected) {
                return prev.filter(f => f.key !== fileKey);
            } else {
                return [...prev, fileObject];
            }
        });
    };

const handleRunWorkflow = (selectedWorkflow, selectedFiles, recordId, setIsCreatingWorkflow, onWorkflowRun) =>
    async () => {
        if (selectedWorkflow && selectedFiles.length > 0) {
            setIsCreatingWorkflow(true);
            try {
                const response = await createWorkflow(recordId, selectedWorkflow.name, selectedFiles);
                if (response.ok) {
                    console.log('Workflow created successfully:', response.data);
                    onWorkflowRun();
                } else {
                    console.error('Failed to create workflow:', response.error);
                }
            } catch (error) {
                console.error('Error creating workflow:', error);
            } finally {
                setIsCreatingWorkflow(false);
            }
        }
    };

const FileSelection = ({ selectedWorkflow, remoteFiles, recordId, onBack, onWorkflowRun }) => {
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [isCreatingWorkflow, setIsCreatingWorkflow] = useState(false);

    return (
        <Stack spacing={3}>
            <Stack direction="row" spacing={2} alignItems="center">
                <Button
                    startIcon={<ArrowBack />}
                    onClick={handleBackToWorkflows(onBack)}
                >
                    Back to Workflows
                </Button>
                <Stack>
                    <Typography variant="h6" component="div">
                        {selectedWorkflow?.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {selectedWorkflow?.mimetype}
                    </Typography>
                </Stack>
            </Stack>

            <Divider />

            <Stack direction="row" justifyContent="space-between" alignItems="center">
                <Typography variant="subtitle1">
                    Select files to process:
                </Typography>
                {selectedFiles.length > 0 && (
                    <Chip
                        size="small"
                        label={`${selectedFiles.length} selected`}
                        color="primary"
                        variant="outlined"
                    />
                )}
            </Stack>

            <Stack spacing={1}>
                {selectedWorkflow?.files.map((file, index) => (
                    <FormControlLabel
                        key={index}
                        control={
                            <Checkbox
                                checked={selectedFiles.some(f => f.key === file)}
                                onChange={() => handleFileToggle(remoteFiles, setSelectedFiles)(file)}
                            />
                        }
                        label={
                            <Stack direction="row" spacing={1} alignItems="center">
                                <Description color="action" />
                                <Typography variant="body1">
                                    {file}
                                </Typography>
                            </Stack>
                        }
                    />
                ))}
            </Stack>

            {selectedFiles.length > 0 && (
                <Stack direction="row" justifyContent="flex-end">
                    <Button
                        variant="contained"
                        startIcon={<PlayArrow />}
                        onClick={handleRunWorkflow(selectedWorkflow, selectedFiles, recordId, setIsCreatingWorkflow, onWorkflowRun)}
                        size="large"
                        disabled={isCreatingWorkflow}
                    >
                        {isCreatingWorkflow
                            ? 'Creating Workflow...'
                            : `Run Workflow (${selectedFiles.length} file${selectedFiles.length !== 1 ? 's' : ''})`
                        }
                    </Button>
                </Stack>
            )}
        </Stack>
    );
};

export default FileSelection;
