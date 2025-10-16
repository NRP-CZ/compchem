import React, { useState } from 'react';
import {
    Paper,
    Tabs,
    Tab
} from '@mui/material';
import { useFormContext } from './context';
import AvailableWorkflowsList from './components/AvailableWorkflowsList';
import FileSelection from './components/FileSelection';
import ActiveWorkflowsList from './components/ActiveWorkflowsList';
import ActiveWorkflowDetail from './components/ActiveWorkflowDetail';

const handleTabChange = (setCurrentTab, setCurrentView, setActiveView) =>
    (_, newValue) => {
        setCurrentTab(newValue);
        setCurrentView('workflows');
        setActiveView('list');
    };

const FormWorkflowsContainer = () => {
    const { record, remoteFiles } = useFormContext();
    const recordId = record.id;

    const [workflowsEnabled, setWorkflowsEnabled] = useState(true);
    const [currentTab, setCurrentTab] = useState(0);
    const [currentView, setCurrentView] = useState('workflows'); // 'workflows' | 'files'
    const [activeView, setActiveView] = useState('list'); // 'list' | 'detail'
    const [selectedWorkflow, setSelectedWorkflow] = useState(null);
    const [selectedActiveWorkflow, setSelectedActiveWorkflow] = useState(null);

    const handleWorkflowSelect = (workflow) => {
        setSelectedWorkflow(workflow);
        setCurrentView('files');
    };

    const handleBackToWorkflows = () => {
        setCurrentView('workflows');
        setSelectedWorkflow(null);
    };

    const handleWorkflowRun = () => {
        setCurrentView('workflows');
        setCurrentTab(1);
    };

    const handleActiveWorkflowSelect = (workflow) => {
        setSelectedActiveWorkflow(workflow);
        setActiveView('detail');
    };

    const handleBackToActiveList = () => {
        setActiveView('list');
        setSelectedActiveWorkflow(null);
    };

    if (!workflowsEnabled) {
        return <></>;
    }

    return (
        <Paper elevation={3} sx={{ p: 3 }}>
            <Tabs value={currentTab} onChange={handleTabChange(setCurrentTab, setCurrentView, setActiveView)} sx={{ mb: 3 }}>
                <Tab label="Available Workflows" />
                <Tab label="Active Workflows" />
            </Tabs>

            {currentTab === 0 && (
                <>
                    {currentView === 'workflows' ? (
                        <AvailableWorkflowsList
                            recordId={recordId}
                            remoteFiles={remoteFiles}
                            onWorkflowSelect={handleWorkflowSelect}
                            setWorkflowsEnabled={setWorkflowsEnabled}
                        />
                    ) : (
                        <FileSelection
                            selectedWorkflow={selectedWorkflow}
                            remoteFiles={remoteFiles}
                            recordId={recordId}
                            onBack={handleBackToWorkflows}
                            onWorkflowRun={handleWorkflowRun}
                        />
                    )}
                </>
            )}

            {currentTab === 1 && (
                <>
                    {activeView === 'list' ? (
                        <ActiveWorkflowsList
                            recordId={recordId}
                            onWorkflowSelect={handleActiveWorkflowSelect}
                        />
                    ) : (
                        <ActiveWorkflowDetail
                            recordId={recordId}
                            selectedActiveWorkflow={selectedActiveWorkflow}
                            onBack={handleBackToActiveList}
                        />
                    )}
                </>
            )}
        </Paper>
    );
};

export default FormWorkflowsContainer;
