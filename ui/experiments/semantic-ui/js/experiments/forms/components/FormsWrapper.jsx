import React from 'react';
import { materialCells, materialRenderers } from '@jsonforms/material-renderers';
import { JsonForms } from '@jsonforms/react';
import { Typography, Stack } from '@mui/material';

import MatrixRenderer from '../renderers/MatrixRenderer'
import MatrixTester from '../renderers/MatrixTester'
import schema from "../schemas/gmx-schema.json"
import uischema from "../schemas/gmx-uischema.json"


const renderers = [
  ...materialRenderers,
  { tester: MatrixTester, renderer: MatrixRenderer },
];

const FormsWrapper = ({data, setData, errors, setErrors, ...other}) => {
    return (
        <>
            <JsonForms
                schema={schema}
                uischema={Object.keys(uischema).length > 0 ?  uischema : undefined}
                data={data}
                renderers={renderers}
                cells={materialCells}
                onChange={({ errors, data }) => {
                    // XXX: Run extra validations here if needed
                    setData(data)
                    setErrors(errors)
                }}
                validationMode='ValidateAndShow'
                {...other}
            />

            {errors && errors.length > 0 && (
                <Stack direction="column" spacing={1} sx={{mt: 3, mb: 3}} color="red">
                    <Typography variant="h4">Errors</Typography>
                    <ul>
                        {errors.map((error, index) => {
                            // For some reason `error.instancePath` was crashing my build
                            // so I had to stringify and parse it to get the value :(
                            const err = JSON.parse(JSON.stringify(error));
                            return(
                                <li key={index}>{err.instancePath}: {err.message}</li>
                            )}
                        )}
                    </ul>
                </Stack>
            )}
        </>
    )
};

export default FormsWrapper;
