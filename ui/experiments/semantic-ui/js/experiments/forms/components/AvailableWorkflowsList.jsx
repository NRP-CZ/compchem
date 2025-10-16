import { useEffect, useState } from 'react';
import {
    Typography,
    Paper,
    Chip,
    Stack,
    Button
} from '@mui/material';
import { PlayArrow } from '@mui/icons-material';
import { fetchAvailableWorkflows } from '../../util/workflowsClient';

const handleWorkflowSelect = (onWorkflowSelect) =>
    (workflow) => {
        onWorkflowSelect(workflow);
    };

const AvailableWorkflowsList = ({ recordId, remoteFiles, onWorkflowSelect, setWorkflowsEnabled }) => {
    const [availableWorkflows, setAvailableWorkflows] = useState([]);

    useEffect(() => {
        const fetchWorkflows = async () => {
            const response = await fetchAvailableWorkflows(recordId, remoteFiles);
            if (response.ok) {
                setWorkflowsEnabled(true);
                setAvailableWorkflows(response.data.workflows);
            } else {
                setWorkflowsEnabled(false);
                setAvailableWorkflows([]);
            }
        };

        fetchWorkflows();
    }, [remoteFiles]);

    return (
        <Stack spacing={3}>
            <Typography variant="h6" gutterBottom>
                Available Workflows
            </Typography>
            <Stack spacing={2}>
                {availableWorkflows.map((workflow, index) => (
                    <Paper key={index} elevation={1}>
                        <Button
                            onClick={() => handleWorkflowSelect(onWorkflowSelect)(workflow)}
                            fullWidth
                            sx={{ textTransform: 'none', p: 2 }}
                        >
                            <Stack direction="row" justifyContent="space-between" alignItems="center" width="100%">
                                <Stack spacing={1} alignItems="flex-start">
                                    <Typography variant="h6" component="div" color="text.primary">
                                        {workflow.name}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        {workflow.mimetype}
                                    </Typography>
                                    <Chip
                                        size="small"
                                        label={`${workflow.files.length} file${workflow.files.length !== 1 ? 's' : ''}`}
                                    />
                                </Stack>
                                <PlayArrow color="primary" />
                            </Stack>
                        </Button>
                    </Paper>
                ))}
            </Stack>
        </Stack>
    );
};

export default AvailableWorkflowsList;
