import { useEffect, useState } from 'react';
import {
    Typography,
    Paper,
    Grid,
    Button,
    Box,
    Divider,
    Chip,
    Modal,
    IconButton,
    CircularProgress,
    Alert,
    Stack
} from '@mui/material';
import {
    ArrowBack,
    Description,
    Receipt,
    Close
} from '@mui/icons-material';
import {
    fetchWorkflowDetail,
    fetchWorkflowLogs
} from '../../util/workflowsClient';

const handleBackToActiveList = (onBack) => () => {
    onBack();
};

const handleOpenLogsModal = (recordId, selectedActiveWorkflow, setLogsModalOpen, setIsLoadingLogs, setLogsError, setWorkflowLogs) =>
    async () => {
        if (!selectedActiveWorkflow?.metadata?.name) return;

        setLogsModalOpen(true);
        setIsLoadingLogs(true);
        setLogsError(null);
        setWorkflowLogs([]);

        try {
            const response = await fetchWorkflowLogs(recordId, selectedActiveWorkflow.metadata.name);
            if (response.ok) {
                setWorkflowLogs(response.data.logs || []);
            } else {
                setLogsError(response.error || 'Failed to fetch logs');
            }
        } catch (error) {
            setLogsError('Error fetching logs: ' + error.message);
        } finally {
            setIsLoadingLogs(false);
        }
    };

const handleCloseLogsModal = (setLogsModalOpen, setWorkflowLogs, setLogsError) =>
    () => {
        setLogsModalOpen(false);
        setWorkflowLogs([]);
        setLogsError(null);
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

const ActiveWorkflowDetail = ({ recordId, selectedActiveWorkflow, onBack }) => {
    const [workflowDetail, setWorkflowDetail] = useState(null);
    const [logsModalOpen, setLogsModalOpen] = useState(false);
    const [workflowLogs, setWorkflowLogs] = useState([]);
    const [isLoadingLogs, setIsLoadingLogs] = useState(false);
    const [logsError, setLogsError] = useState(null);

    useEffect(() => {
        const fetchDetail = async () => {
            if (selectedActiveWorkflow?.metadata?.name) {
                const response = await fetchWorkflowDetail(recordId, selectedActiveWorkflow.metadata.name);
                if (response.ok) {
                    setWorkflowDetail(response.data);
                }
            }
        };

        fetchDetail();
    }, [selectedActiveWorkflow]);

    const renderLogsModal = () => (
        <Modal
            open={logsModalOpen}
            onClose={handleCloseLogsModal(setLogsModalOpen, setWorkflowLogs, setLogsError)}
            aria-labelledby="workflow-logs-modal"
            aria-describedby="workflow-logs-content"
        >
            <Box sx={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                width: '95%',
                maxWidth: '1400px',
                maxHeight: '80vh',
                bgcolor: 'background.paper',
                boxShadow: 24,
                p: 0,
                borderRadius: 1,
                overflow: 'hidden'
            }}>
                <Box sx={{
                    p: 2,
                    borderBottom: 1,
                    borderColor: 'divider',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between'
                }}>
                    <Box>
                        <Typography variant="h6" component="h2">
                            Workflow Logs
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            {selectedActiveWorkflow?.metadata.name}
                        </Typography>
                    </Box>
                    <IconButton onClick={handleCloseLogsModal(setLogsModalOpen, setWorkflowLogs, setLogsError)}>
                        <Close />
                    </IconButton>
                </Box>

                <Box sx={{
                    p: 2,
                    maxHeight: 'calc(90vh - 100px)',
                    overflowY: 'auto'
                }}>
                    {isLoadingLogs && (
                        <Box sx={{ display: 'flex', justifyContent: 'center', py: 4 }}>
                            <CircularProgress />
                        </Box>
                    )}

                    {logsError && (
                        <Alert severity="error" sx={{ mb: 2 }}>
                            {logsError}
                        </Alert>
                    )}

                    {!isLoadingLogs && !logsError && workflowLogs.length === 0 && (
                        <Box sx={{ textAlign: 'center', py: 4 }}>
                            <Typography variant="body2" color="text.secondary">
                                No logs found for this workflow
                            </Typography>
                        </Box>
                    )}

                    {!isLoadingLogs && workflowLogs.length > 0 && (
                        <Box>
                            <Typography variant="subtitle2" sx={{ mb: 2 }}>
                                {workflowLogs.length} log entries
                            </Typography>
                            <Box
                                sx={{
                                    backgroundColor: '#1e1e1e',
                                    color: '#ffffff',
                                    fontFamily: 'Consolas, Monaco, "Courier New", monospace',
                                    fontSize: '0.75rem',
                                    lineHeight: 1.4,
                                    p: 2,
                                    borderRadius: 1,
                                    maxHeight: 'calc(90vh - 300px)',
                                    overflowY: 'auto',
                                    border: '1px solid #333'
                                }}
                            >
                                <Box component="pre" sx={{ margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>
                                    {workflowLogs.map((logEntry, index) => {
                                        const podName = logEntry.result?.podName || 'unknown';
                                        const content = logEntry.result?.content || '';

                                        const formattedLine = content
                                            ? `${podName}: ${content}`
                                            : `${podName}:`;

                                        return (
                                            <Box key={index} component="span">
                                                {formattedLine}
                                                {'\n'}
                                            </Box>
                                        );
                                    })}
                                </Box>
                            </Box>
                        </Box>
                    )}
                </Box>
            </Box>
        </Modal>
    );

    return (
        <Stack spacing={3}>
            <Stack spacing={2}>
                <Stack spacing={1}>
                    <Typography variant="h6" component="div">
                        {selectedActiveWorkflow?.metadata.name}
                    </Typography>
                    <Box alignSelf="flex-start">
                        <Chip
                            size="small"
                            label={selectedActiveWorkflow?.status.phase}
                            color={getStatusColor(selectedActiveWorkflow?.status.phase)}
                            variant="outlined"
                        />
                    </Box>
                </Stack>

                <Stack direction="row" spacing={2}>
                    <Button
                        startIcon={<ArrowBack />}
                        onClick={handleBackToActiveList(onBack)}
                    >
                        Back to Active Workflows
                    </Button>
                    <Button
                        variant="outlined"
                        startIcon={<Receipt />}
                        onClick={handleOpenLogsModal(recordId, selectedActiveWorkflow, setLogsModalOpen, setIsLoadingLogs, setLogsError, setWorkflowLogs)}
                    >
                        View Logs
                    </Button>
                </Stack>
            </Stack>

            <Divider />

            <Paper elevation={1} sx={{ p: 2 }}>
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

            <Stack spacing={1}>
                <Typography variant="subtitle1" gutterBottom>
                    Processed Files ({workflowDetail?.files.length || 0})
                </Typography>
                <Grid container spacing={1} direction="column">
                    {workflowDetail?.files.map((file, index) => (
                        <Grid item xs={12} key={index}>
                            <Paper elevation={1} sx={{ p: 2 }}>
                                <Stack direction="row" spacing={1} alignItems="center">
                                    <Description color="action" />
                                    <Typography variant="body1">
                                        {file}
                                    </Typography>
                                </Stack>
                            </Paper>
                        </Grid>
                    ))}
                    {(!workflowDetail?.files || workflowDetail.files.length === 0) && (
                        <Grid item xs={12}>
                            <Stack alignItems="center" py={2}>
                                <Typography variant="body2" color="text.secondary">
                                    No files found for this workflow
                                </Typography>
                            </Stack>
                        </Grid>
                    )}
                </Grid>
            </Stack>

            {renderLogsModal()}
        </Stack>
    );
};

export default ActiveWorkflowDetail;
