import React, { useState } from 'react'
import { Paper, Typography } from '@mui/material'

import FormsWrapper from './FormsWrapper'
import schema from '../schemas/experiment-schema.json'

const ExperimentEditor = ({ data, setData }) => {
    return (
        <>
            <Typography variant="h3">Experiment metadata</Typography>
            <Paper elevation={3} sx={{ p: 2 }}>
                <FormsWrapper
                    schema={schema}
                    uischema={{}}
                    data={data}
                    setData={setData}
                />
            </Paper>
        </>
    )
}

export default ExperimentEditor
