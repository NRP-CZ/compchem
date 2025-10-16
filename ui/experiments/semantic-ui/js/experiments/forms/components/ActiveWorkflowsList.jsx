import React, { useEffect, useState } from 'react';
import {
    Typography,
    Paper,
    Grid,
    Button,
    Chip,
    Stack,
    ButtonBase
} from '@mui/material';
import {
    History,
    Schedule,
    NavigateNext,
    NavigateBefore
} from '@mui/icons-material';
import { listRecordWorkflows } from '../../util/workflowsClient';

const handleStatusToggle = (setSelectedStatuses, setSkip) =>
    (status) => {
        setSelectedStatuses(prev => {
            const newStatuses = prev.includes(status)
                ? prev.filter(s => s !== status)
                : [...prev, status];

            setSkip(0);
            return newStatuses;
        });
    };

const handleClearFilters = (setSelectedStatuses, setSkip) =>
    () => {
        setSelectedStatuses([]);
        setSkip(0);
    };

const handleActiveWorkflowSelect = (onWorkflowSelect) =>
    (workflow) => {
        onWorkflowSelect(workflow);
    };

const handleNextPage = (workflowsMetadata, setSkip) =>
    () => {
        if (workflowsMetadata?.continue) {
            setSkip(parseInt(workflowsMetadata.continue));
        }
    };

const handlePreviousPage = (skip, setSkip) =>
    () => {
        setSkip(Math.max(0, skip - 5));
    };

const getStatusColor = (phase) => {
    switch (phase) {
        case 'Succeeded': return 'success';
        case 'Running': return 'info';
        case 'Pending': return 'warning';
        case 'Failed': return 'error';
        case 'Error': return 'error';
        default: return 'default';
    }
};

const formatDate = (dateString) => {
    if (!dateString) return 'N/A';
    return new Date(dateString).toLocaleString();
};

const ActiveWorkflowsList = ({ recordId, onWorkflowSelect }) => {
    const [activeWorkflows, setActiveWorkflows] = useState([]);
    const [skip, setSkip] = useState(0);
    const [workflowsMetadata, setWorkflowsMetadata] = useState(null);
    const [selectedStatuses, setSelectedStatuses] = useState([]);

    const availableStatuses = ['Error', 'Pending', 'Running', 'Succeeded', 'Failed'];

    useEffect(() => {
        const fetchActiveWorkflows = async () => {
            const statusFilter = selectedStatuses.length > 0 ? selectedStatuses : [];
            const response = await listRecordWorkflows(recordId, skip, 5, statusFilter);
            if (response.ok) {
                setActiveWorkflows(response.data.items || []);
                setWorkflowsMetadata(response.data.metadata || null);
            }
        };

        fetchActiveWorkflows();
    }, [recordId, skip, selectedStatuses]);

    return (
        <Stack>
            <Typography variant="h6" gutterBottom>
                Active Workflows
            </Typography>


            <Grid container spacing={2} direction="column">
                <Grid item xs={12} key={"filters"}>
                    <Paper elevation={1} sx={{ p: 2 }}>
                        <Stack spacing={2}>
                            <Stack direction="row" justifyContent="space-between" alignItems="center">
                                <Typography variant="subtitle1">
                                    Filter by Status:
                                </Typography>
                                {selectedStatuses.length > 0 && (
                                    <Chip
                                        size="small"
                                        label={`${selectedStatuses.length} selected`}
                                        color="primary"
                                        variant="outlined"
                                    />
                                )}
                            </Stack>
                            <Stack direction="row" flexWrap="wrap" gap={1}>
                                {availableStatuses.map((status) => (
                                    <Chip
                                        key={status}
                                        label={status}
                                        onClick={() => handleStatusToggle(setSelectedStatuses, setSkip)(status)}
                                        color={selectedStatuses.includes(status) ? getStatusColor(status) : 'default'}
                                        variant={selectedStatuses.includes(status) ? 'filled' : 'outlined'}
                                        clickable
                                    />
                                ))}
                            </Stack>
                            {selectedStatuses.length > 0 && (
                                <Button
                                    size="small"
                                    onClick={handleClearFilters(setSelectedStatuses, setSkip)}
                                    variant="text"
                                >
                                    Clear Filters
                                </Button>
                            )}
                        </Stack>
                    </Paper>
                </Grid>
                {activeWorkflows.map((workflow, index) => (
                    <Grid item xs={12} key={index}>
                        <ButtonBase
                            onClick={() => handleActiveWorkflowSelect(onWorkflowSelect)(workflow)}
                            sx={{ width: '100%', borderRadius: 1 }}
                        >
                            <Paper elevation={1} sx={{ p: 2, width: '100%' }}>
                                <Stack direction="row" justifyContent="space-between" alignItems="center" width="100%">
                                    <Stack spacing={1} flex={1} alignItems="flex-start">
                                        <Typography variant="h6" component="div">
                                            {workflow.metadata.name}
                                        </Typography>
                                        <Stack direction="row" spacing={1} alignItems="center">
                                            <Chip
                                                size="small"
                                                label={workflow.status.phase}
                                                color={getStatusColor(workflow.status.phase)}
                                                variant="outlined"
                                            />
                                            {workflow.status.progress && (
                                                <Chip
                                                    size="small"
                                                    label={`Progress: ${workflow.status.progress}`}
                                                    variant="outlined"
                                                />
                                            )}
                                        </Stack>
                                        <Typography variant="body2" color="text.secondary">
                                            Started: {formatDate(workflow.status.startedAt)}
                                        </Typography>
                                        {workflow.status.finishedAt && (
                                            <Typography variant="body2" color="text.secondary">
                                                Finished: {formatDate(workflow.status.finishedAt)}
                                            </Typography>
                                        )}
                                    </Stack>
                                    <History color="primary" />
                                </Stack>
                            </Paper>
                        </ButtonBase>
                    </Grid>
                ))}
                {activeWorkflows.length === 0 && (
                    <Grid item xs={12}>
                        <Stack alignItems="center" spacing={2} py={4}>
                            <Schedule fontSize="large" color="action" />
                            <Typography variant="h6" color="text.secondary">
                                No active workflows found
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                Run a workflow from the Available Workflows tab to see it here
                            </Typography>
                        </Stack>
                    </Grid>
                )}
            </Grid>

            {(skip > 0 || workflowsMetadata?.continue) && (
                <Stack direction="row" justifyContent="center" spacing={2} alignItems="center">
                    <Button
                        startIcon={<NavigateBefore />}
                        onClick={handlePreviousPage(skip, setSkip)}
                        disabled={skip === 0}
                        variant="outlined"
                    >
                        Previous
                    </Button>
                    <Typography variant="body2" color="text.secondary">
                        Page {Math.floor(skip / 5) + 1}
                    </Typography>
                    <Button
                        endIcon={<NavigateNext />}
                        onClick={handleNextPage(workflowsMetadata, setSkip)}
                        disabled={!workflowsMetadata?.continue}
                        variant="outlined"
                    >
                        Next
                    </Button>
                </Stack>
            )}
        </Stack>
    );
};

export default ActiveWorkflowsList;
