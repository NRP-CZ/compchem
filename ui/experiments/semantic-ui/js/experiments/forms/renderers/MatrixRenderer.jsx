import React from 'react';

import { withJsonFormsArrayLayoutProps, useJsonForms } from '@jsonforms/react';
import { MaterialNumberCell } from '@jsonforms/material-renderers';
import { Tooltip, IconButton } from '@mui/material';
import { Delete as DeleteIcon } from '@mui/icons-material';

import ArrayLayoutToolbar from './jsonfroms-components/ArrayToolbar';

/**
 * Modified version of the default material renderer:
 * https://github.com/eclipsesource/jsonforms/blob/master/packages/material-renderers/src/layouts/MaterialArrayLayout.tsx
 */

const range = (start, end = 0) => {
  return Array.from({ length: end - start }, (_, i) => start + i);
}

const MatrixRenderer = (props) => {
    const {
      enabled,
      data,
      path,
      schema,
      uischema,
      errors,
      addItem,
      removeItems,
      renderers,
      cells,
      label,
      required,
      rootSchema,
      config,
      uischemas,
      translations,
      description,
    } = props;

    const ctx = useJsonForms()
    const rowCount = schema.minLength || 0;
    const colCount = schema.minItems || 0;

    const innerCreateDefaultValue = () => {
      return new Array(colCount).fill(0);
    }

    const addWithCheck = (path, value) => {
      if (!data) {
        return addItem(path, value);
      }
      return () => {};
    }

    const removeMatrix = (path) => {
      if (data && removeItems) {
        return removeItems(path, range(0, rowCount));
      }
      return () => {};
    }

    // get actual data from the context
    let matrixData = path.split('.').reduce((obj, attr) => (obj && obj[attr]) ? obj[attr] : [], ctx.core?.data);

    if (data) {
      // fill missing rows
      while (matrixData && matrixData.length < rowCount) {
        matrixData.push(new Array(colCount).fill(0));
      }

      // fill missing columns
      for (let i = 0; i < matrixData.length; i++) {
        while (matrixData[i].length < colCount) {
          matrixData[i].push(0);
        }
      }
    }

    return (
      <div style={{ marginBottom: '25px' }}>
        <ArrayLayoutToolbar
          translations={translations}
          label={label}
          description={description || ''}
          errors={errors}
          path={path}
          enabled={enabled}
          addItem={addWithCheck}
          removeMatrix={removeMatrix}
          createDefault={innerCreateDefaultValue}
        />

        {data != 0 && (
          <table>
          <tbody>
            {matrixData.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {Array.from(row).map((cell, cellIndex) => (
                  <td key={cellIndex}>
                    <MaterialNumberCell
                      key={cellIndex}
                      path={`${path}.${rowIndex}.${cellIndex}`}
                      schema={schema}
                      uischema={uischema}
                    />
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
          </table>
        )}
      </div>
    );
};

export default withJsonFormsArrayLayoutProps(MatrixRenderer);
