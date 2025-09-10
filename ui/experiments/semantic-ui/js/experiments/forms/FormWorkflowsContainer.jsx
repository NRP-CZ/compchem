import React, { useEffect, useState } from 'react';
import { 
    Typography, 
    Paper, 
    Grid, 
    Button, 
    Checkbox, 
    FormControlLabel, 
    FormControl, 
    Box,
    Divider,
    Chip,
    Tabs,
    Tab
} from '@mui/material';
import { ArrowBack, PlayArrow, Description, History, Schedule, NavigateNext, NavigateBefore } from '@mui/icons-material';
import { fetchAvailableWorkflows, listRecordWorkflows, fetchWorkflowDetail, createWorkflow } from '../util/workflowsClient';
import { useFormContext } from './context';

const FormWorkflowsContainer = () => {
    const { record, remoteFiles } = useFormContext();
    const recordId = record.id;
    
    // State management
    const [currentTab, setCurrentTab] = useState(0);
    
    // Available workflows tab state
    const [availableWorkflows, setAvailableWorkflows] = useState([]); 
    const [currentView, setCurrentView] = useState('workflows'); // 'workflows' | 'files'
    const [selectedWorkflow, setSelectedWorkflow] = useState(null);
    const [selectedFiles, setSelectedFiles] = useState([]);
    const [isCreatingWorkflow, setIsCreatingWorkflow] = useState(false);
    
    // Active workflows tab state
    const [activeWorkflows, setActiveWorkflows] = useState([]);
    const [activeView, setActiveView] = useState('list'); // 'list' | 'detail'
    const [selectedActiveWorkflow, setSelectedActiveWorkflow] = useState(null);
    const [workflowDetail, setWorkflowDetail] = useState(null);
    const [skip, setSkip] = useState(0);
    const [workflowsMetadata, setWorkflowsMetadata] = useState(null);
    const [selectedStatuses, setSelectedStatuses] = useState([]);
    
    useEffect(() => {
        const fetchWorkflows = async () => {
            const response = await fetchAvailableWorkflows(remoteFiles);
            if (response.ok) {
                setAvailableWorkflows(response.data.workflows);
            }
        };
        
        fetchWorkflows();
    }, [remoteFiles]);

    useEffect(() => {
        const fetchActiveWorkflows = async () => {
            // Convert selectedStatuses array to the format expected by API
            const statusFilter = selectedStatuses.length > 0 ? selectedStatuses : [];
            const response = await listRecordWorkflows(recordId, skip, 5, statusFilter);
            if (response.ok) {
                setActiveWorkflows(response.data.items || []);
                setWorkflowsMetadata(response.data.metadata || null);
            }
        };
        
        if (currentTab === 1) {
            fetchActiveWorkflows();
        }
    }, [recordId, currentTab, skip, selectedStatuses]);

    // Tab change handler
    const handleTabChange = (event, newValue) => {
        setCurrentTab(newValue);
        // Reset views when switching tabs
        setCurrentView('workflows');
        setActiveView('list');
        setSkip(0); // Reset pagination
        setSelectedStatuses([]); // Reset status filter
    };

    // Available workflows event handlers
    const handleWorkflowSelect = (workflow) => {
        setSelectedWorkflow(workflow);
        setSelectedFiles([]); // Reset file selection
        setCurrentView('files');
    };

    const handleBackToWorkflows = () => {
        setCurrentView('workflows');
        setSelectedWorkflow(null);
        setSelectedFiles([]);
    };

    const handleFileToggle = (fileKey) => {
        // Find the full file object from remoteFiles
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

    const handleRunWorkflow = async () => {
        if (selectedWorkflow && selectedFiles.length > 0) {
            setIsCreatingWorkflow(true);
            try {
                // Extract just the keys from selected file objects for the API
                const response = await createWorkflow(recordId, selectedWorkflow.name, selectedFiles);
                if (response.ok) {
                    // Success - reset form and switch to Active Workflows tab
                    setSelectedFiles([]);
                    setCurrentView('workflows');
                    setCurrentTab(1); // Switch to Active Workflows tab
                    setSkip(0); // Reset to first page
                    console.log('Workflow created successfully:', response.data);
                } else {
                    console.error('Failed to create workflow:', response.error);
                    // TODO: Show error message to user
                }
            } catch (error) {
                console.error('Error creating workflow:', error);
                // TODO: Show error message to user
            } finally {
                setIsCreatingWorkflow(false);
            }
        }
    };

    // Active workflows event handlers
    const handleActiveWorkflowSelect = async (workflow) => {
        setSelectedActiveWorkflow(workflow);
        const response = await fetchWorkflowDetail(workflow.metadata.name);
        if (response.ok) {
            setWorkflowDetail(response.data);
        }
        setActiveView('detail');
    };

    const handleBackToActiveList = () => {
        setActiveView('list');
        setSelectedActiveWorkflow(null);
        setWorkflowDetail(null);
    };

    // Pagination handlers
    const handleNextPage = () => {
        if (workflowsMetadata?.continue) {
            setSkip(parseInt(workflowsMetadata.continue));
        }
    };

    const handlePreviousPage = () => {
        setSkip(Math.max(0, skip - 5));
    };

    // Status filter handlers
    const handleStatusToggle = (status) => {
        setSelectedStatuses(prev => {
            const newStatuses = prev.includes(status) 
                ? prev.filter(s => s !== status)
                : [...prev, status];
            
            // Reset to first page when filter changes
            setSkip(0);
            return newStatuses;
        });
    };

    // Available workflow statuses
    const availableStatuses = ['Error', 'Pending', 'Running', 'Succeeded', 'Failed'];

    // Helper functions
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

    // Render workflow list view
    const renderWorkflowList = () => (
        <>
            <Typography variant="h6" gutterBottom sx={{ mb: 3 }}>
                Available Workflows
            </Typography>
            <Grid container spacing={2} direction="column">
                {availableWorkflows.map((workflow, index) => (
                    <Grid item xs={12} key={index}>
                        <Paper 
                            elevation={1} 
                            sx={{ 
                                p: 2, 
                                cursor: 'pointer',
                                transition: 'all 0.2s ease-in-out',
                                '&:hover': {
                                    elevation: 3,
                                    backgroundColor: 'action.hover'
                                }
                            }}
                            onClick={() => handleWorkflowSelect(workflow)}
                        >
                            <Box display="flex" alignItems="center" justifyContent="space-between">
                                <Box>
                                    <Typography variant="h6" component="div">
                                        {workflow.name}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary" sx={{ mt: 0.5 }}>
                                        {workflow.mimetype}
                                    </Typography>
                                    <Box sx={{ mt: 1 }}>
                                        <Chip 
                                            size="small" 
                                            label={`${workflow.files.length} file${workflow.files.length !== 1 ? 's' : ''}`} 
                                            variant="outlined"
                                        />
                                    </Box>
                                </Box>
                                <PlayArrow color="primary" />
                            </Box>
                        </Paper>
                    </Grid>
                ))}
            </Grid>
        </>
    );

    // Render file selection view
    const renderFileSelection = () => (
        <>
            <Box display="flex" alignItems="center" sx={{ mb: 3 }}>
                <Button
                    startIcon={<ArrowBack />}
                    onClick={handleBackToWorkflows}
                    sx={{ mr: 2 }}
                >
                    Back to Workflows
                </Button>
                <Box>
                    <Typography variant="h6" component="div">
                        {selectedWorkflow?.name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {selectedWorkflow?.mimetype}
                    </Typography>
                </Box>
            </Box>

            <Divider sx={{ mb: 3 }} />

            <Box display="flex" alignItems="center" justifyContent="space-between" sx={{ mb: 2 }}>
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
            </Box>

            <FormControl component="fieldset" sx={{ width: '100%' }}>
                <Grid container spacing={1} direction="column">
                    {selectedWorkflow?.files.map((file, index) => (
                        <Grid item xs={12} key={index}>
                            <Paper 
                                elevation={1} 
                                sx={{ 
                                    p: 2,
                                    backgroundColor: selectedFiles.some(f => f.key === file) ? 'action.selected' : 'background.paper',
                                    cursor: 'pointer',
                                    transition: 'background-color 0.2s ease-in-out',
                                    '&:hover': {
                                        backgroundColor: selectedFiles.some(f => f.key === file) ? 'action.selected' : 'action.hover'
                                    }
                                }}
                                onClick={() => handleFileToggle(file)}
                            >
                                <FormControlLabel
                                    control={
                                        <Checkbox 
                                            checked={selectedFiles.some(f => f.key === file)}
                                            onChange={(e) => e.stopPropagation()}
                                        />
                                    }
                                    label={
                                        <Box display="flex" alignItems="center">
                                            <Description sx={{ mr: 1, color: 'text.secondary' }} />
                                            <Typography variant="body1">
                                                {file}
                                            </Typography>
                                        </Box>
                                    }
                                    sx={{ margin: 0, width: '100%' }}
                                />
                            </Paper>
                        </Grid>
                    ))}
                </Grid>
            </FormControl>

            {selectedFiles.length > 0 && (
                <Box sx={{ mt: 3, display: 'flex', justifyContent: 'flex-end' }}>
                    <Button
                        variant="contained"
                        startIcon={<PlayArrow />}
                        onClick={handleRunWorkflow}
                        size="large"
                        disabled={isCreatingWorkflow}
                    >
                        {isCreatingWorkflow 
                            ? 'Creating Workflow...' 
                            : `Run Workflow (${selectedFiles.length} file${selectedFiles.length !== 1 ? 's' : ''})`
                        }
                    </Button>
                </Box>
            )}
        </>
    );

    // Render active workflows list view
    const renderActiveWorkflowsList = () => (
        <>
            <Typography variant="h6" gutterBottom sx={{ mb: 3 }}>
                Active Workflows
            </Typography>

            {/* Status Filter */}
            <Paper elevation={1} sx={{ p: 2, mb: 3 }}>
                <Box display="flex" alignItems="center" justifyContent="space-between" sx={{ mb: 2 }}>
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
                </Box>
                <Box display="flex" flexWrap="wrap" gap={1}>
                    {availableStatuses.map((status) => (
                        <Chip
                            key={status}
                            label={status}
                            onClick={() => handleStatusToggle(status)}
                            color={selectedStatuses.includes(status) ? getStatusColor(status) : 'default'}
                            variant={selectedStatuses.includes(status) ? 'filled' : 'outlined'}
                            clickable
                            sx={{ cursor: 'pointer' }}
                        />
                    ))}
                </Box>
                {selectedStatuses.length > 0 && (
                    <Box sx={{ mt: 2 }}>
                        <Button 
                            size="small" 
                            onClick={() => {
                                setSelectedStatuses([]);
                                setSkip(0);
                            }}
                            variant="text"
                        >
                            Clear Filters
                        </Button>
                    </Box>
                )}
            </Paper>

            <Grid container spacing={2} direction="column">
                {activeWorkflows.map((workflow, index) => (
                    <Grid item xs={12} key={index}>
                        <Paper 
                            elevation={1} 
                            sx={{ 
                                p: 2, 
                                cursor: 'pointer',
                                transition: 'all 0.2s ease-in-out',
                                '&:hover': {
                                    elevation: 3,
                                    backgroundColor: 'action.hover'
                                }
                            }}
                            onClick={() => handleActiveWorkflowSelect(workflow)}
                        >
                            <Box display="flex" alignItems="center" justifyContent="space-between">
                                <Box sx={{ flex: 1 }}>
                                    <Typography variant="h6" component="div">
                                        {workflow.metadata.name}
                                    </Typography>
                                    <Box sx={{ mt: 1, display: 'flex', gap: 1, alignItems: 'center' }}>
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
                                    </Box>
                                    <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                                        Started: {formatDate(workflow.status.startedAt)}
                                    </Typography>
                                    {workflow.status.finishedAt && (
                                        <Typography variant="body2" color="text.secondary">
                                            Finished: {formatDate(workflow.status.finishedAt)}
                                        </Typography>
                                    )}
                                </Box>
                                <History color="primary" />
                            </Box>
                        </Paper>
                    </Grid>
                ))}
                {activeWorkflows.length === 0 && (
                    <Grid item xs={12}>
                        <Box textAlign="center" sx={{ py: 4 }}>
                            <Schedule sx={{ fontSize: 48, color: 'text.secondary', mb: 2 }} />
                            <Typography variant="h6" color="text.secondary">
                                No active workflows found
                            </Typography>
                            <Typography variant="body2" color="text.secondary">
                                Run a workflow from the Available Workflows tab to see it here
                            </Typography>
                        </Box>
                    </Grid>
                )}
            </Grid>

            {/* Pagination Controls */}
            {(skip > 0 || workflowsMetadata?.continue) && (
                <Box sx={{ mt: 3, display: 'flex', justifyContent: 'center', gap: 2 }}>
                    <Button
                        startIcon={<NavigateBefore />}
                        onClick={handlePreviousPage}
                        disabled={skip === 0}
                        variant="outlined"
                    >
                        Previous
                    </Button>
                    <Typography variant="body2" sx={{ alignSelf: 'center', color: 'text.secondary' }}>
                        Page {Math.floor(skip / 5) + 1}
                    </Typography>
                    <Button
                        endIcon={<NavigateNext />}
                        onClick={handleNextPage}
                        disabled={!workflowsMetadata?.continue}
                        variant="outlined"
                    >
                        Next
                    </Button>
                </Box>
            )}
        </>
    );

    // Render active workflow detail view
    const renderActiveWorkflowDetail = () => (
        <>
            <Box display="flex" alignItems="center" sx={{ mb: 3 }}>
                <Button
                    startIcon={<ArrowBack />}
                    onClick={handleBackToActiveList}
                    sx={{ mr: 2 }}
                >
                    Back to Active Workflows
                </Button>
                <Box>
                    <Typography variant="h6" component="div">
                        {selectedActiveWorkflow?.metadata.name}
                    </Typography>
                    <Box sx={{ mt: 1 }}>
                        <Chip 
                            size="small" 
                            label={selectedActiveWorkflow?.status.phase}
                            color={getStatusColor(selectedActiveWorkflow?.status.phase)}
                            variant="outlined"
                        />
                    </Box>
                </Box>
            </Box>

            <Divider sx={{ mb: 3 }} />

            {/* Status Information */}
            <Paper elevation={1} sx={{ p: 2, mb: 3 }}>
                <Typography variant="subtitle1" gutterBottom>
                    Status Information
                </Typography>
                <Grid container spacing={2}>
                    <Grid item xs={12} sm={6}>
                        <Typography variant="body2" color="text.secondary">
                            Phase
                        </Typography>
                        <Typography variant="body1">
                            {selectedActiveWorkflow?.status.phase}
                        </Typography>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Typography variant="body2" color="text.secondary">
                            Progress
                        </Typography>
                        <Typography variant="body1">
                            {selectedActiveWorkflow?.status.progress || 'N/A'}
                        </Typography>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Typography variant="body2" color="text.secondary">
                            Started At
                        </Typography>
                        <Typography variant="body1">
                            {formatDate(selectedActiveWorkflow?.status.startedAt)}
                        </Typography>
                    </Grid>
                    <Grid item xs={12} sm={6}>
                        <Typography variant="body2" color="text.secondary">
                            Finished At
                        </Typography>
                        <Typography variant="body1">
                            {formatDate(selectedActiveWorkflow?.status.finishedAt)}
                        </Typography>
                    </Grid>
                </Grid>
            </Paper>

            {/* Files Information */}
            <Typography variant="subtitle1" gutterBottom>
                Processed Files ({workflowDetail?.files.length || 0})
            </Typography>
            <Grid container spacing={1} direction="column">
                {workflowDetail?.files.map((file, index) => (
                    <Grid item xs={12} key={index}>
                        <Paper elevation={1} sx={{ p: 2 }}>
                            <Box display="flex" alignItems="center">
                                <Description sx={{ mr: 1, color: 'text.secondary' }} />
                                <Typography variant="body1">
                                    {file}
                                </Typography>
                            </Box>
                        </Paper>
                    </Grid>
                ))}
                {(!workflowDetail?.files || workflowDetail.files.length === 0) && (
                    <Grid item xs={12}>
                        <Box textAlign="center" sx={{ py: 2 }}>
                            <Typography variant="body2" color="text.secondary">
                                No files found for this workflow
                            </Typography>
                        </Box>
                    </Grid>
                )}
            </Grid>
        </>
    );

    return (
        <Paper elevation={3} sx={{ p: 3 }}>
            <Tabs value={currentTab} onChange={handleTabChange} sx={{ mb: 3 }}>
                <Tab label="Available Workflows" />
                <Tab label="Active Workflows" />
            </Tabs>
            
            {currentTab === 0 && (
                <>
                    {currentView === 'workflows' ? renderWorkflowList() : renderFileSelection()}
                </>
            )}
            
            {currentTab === 1 && (
                <>
                    {activeView === 'list' ? renderActiveWorkflowsList() : renderActiveWorkflowDetail()}
                </>
            )}
        </Paper>
    );
};

export default FormWorkflowsContainer;
