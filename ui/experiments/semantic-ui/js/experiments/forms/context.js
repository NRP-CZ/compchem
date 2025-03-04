import React, { createContext, useEffect, useContext, useState } from "react";

import { listFilesOfRecord } from "../util/apiClient";
import useConfirmDialog from './components/ConfirmDialog';

export const FormContext = createContext();


export const FormContextProvider = ({ initialRecord, children }) => {
    const [record, setRecord] = useState(initialRecord);
    const [localFiles, setLocalFiles] = useState({});
    const [remoteFiles, setRemoteFiles] = useState([]);
    const [deletedFiles, setDeletedFiles] = useState([]);
    const [simulationFiles, setSimulationFiles] = useState([]);
    const [files, setFiles] = useState([]);

    const [showDialog, ConfirmDialog] = useConfirmDialog();

    useEffect(() => {
        // merge localFiles with remoteFiles, ensuring no duplicates
        const localFileNames = Object.keys(localFiles);
        const newFiles = [...localFileNames];

        for (const fileName of remoteFiles)
            if (!localFiles.hasOwnProperty(fileName))
                newFiles.push(fileName);

        setFiles(newFiles);
    }, [localFiles, remoteFiles]);

    useEffect(() => {
        // load remoteFiles if editing record
        if (record.id) {
            listFilesOfRecord(record.id).then(({ data: { entries = [] } = {} }) => {
                setRemoteFiles(entries.map(({ key }) => key));
            });
        }
    }, []);

    useEffect(() => {
        let simulations = record.metadata?.simulations || [];

        setSimulationFiles((prev) => {
            try {
                return simulations.map(simulation => simulation.file_identification.name)
            } catch {
                return prev
            }
        });
    }, [record.metadata.simulations]);

    return (
        <FormContext.Provider value={{
            record, setRecord,
            localFiles, setLocalFiles,
            remoteFiles, setRemoteFiles,
            deletedFiles, setDeletedFiles,
            files, setFiles,
            simulationFiles,
            showDialog,
        }}>
            {children}
            <ConfirmDialog />
        </FormContext.Provider>
    );
};

export const useFormContext = () => {
    const context = useContext(FormContext);

    if (!context)
        throw new Error("useFormContext must be used within a FormContextProvider");

    return context;
};
