import React, { useState } from 'react'

import Dropzone from "./components/Dropzone"
import FileMetadataEditor from "./components/FileMetadataEditor"


const FormFieldsContainer = ({ record }) => {
    const [fileMetadata, setFileMetadata] = useState({})    // {filename: {metadata}}
    const [fileErrors, setFileErrors] = useState({})        // {filename: [errors]}

    return (
        <div>
            <Dropzone
                fileMetadata={fileMetadata}
                setFileMetadata={setFileMetadata}
            />

            <FileMetadataEditor
                fileMetadata={fileMetadata}
                setFileMetadata={setFileMetadata}
                fileErrors={fileErrors}
                setFileErrors={setFileErrors}
            />

            <h1>DEBUG</h1>
            <pre>
                {JSON.stringify(record, null, 4)}
            </pre>
        </div>
    )
}

export default FormFieldsContainer
