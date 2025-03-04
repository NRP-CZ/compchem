import { FormHelperText, Grid, IconButton, Stack, Toolbar, Tooltip, Typography } from '@mui/material';
import { Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import React from 'react';

import ValidationIcon from './ValidationIcon';


const ArrayLayoutToolbar = React.memo(function ArrayLayoutToolbar({
  label,
  description,
  errors,
  addItem,
  removeMatrix,
  path,
  enabled,
  createDefault,
  translations,
}) {
  return (
    <Toolbar disableGutters={true}>
      <Stack>
        <Grid container alignItems='center' justifyContent='space-between'>
          <Grid item>
            <Grid
              container
              justifyContent={'flex-start'}
              alignItems={'center'}
              spacing={2}
            >
              <Grid item>
                <Typography variant={'h6'}>{label}</Typography>
              </Grid>
              <Grid item>
                {errors.length !== 0 && (
                  <Grid item>
                    <ValidationIcon
                      id='tooltip-validation'
                      errorMessages={errors}
                    />
                  </Grid>
                )}
              </Grid>
            </Grid>
          </Grid>
          {enabled && (
            <Grid item>
              <Grid container>
                <Grid item>
                  <Tooltip
                    id='tooltip-add'
                    title={translations?.addTooltip || 'Add Item'}
                    placement='bottom'
                  >
                    <IconButton
                      aria-label={translations?.addTooltip || 'Add Item'}
                      onClick={addItem(path, createDefault())}
                      size='large'
                    >
                      <AddIcon />
                    </IconButton>
                  </Tooltip>
                </Grid>
                <Grid item>
                  <Tooltip
                    id='tooltip-remove'
                    title={translations?.removeTooltip  || 'Remove Item'}
                    placement='bottom'
                  >
                    <IconButton
                      onClick={removeMatrix(path)}
                      style={{ float: 'right' }}
                      aria-label={translations?.removeAriaLabel || 'Remove Item'}
                      size='large'
                    >
                      <DeleteIcon />
                    </IconButton>
                  </Tooltip>
                </Grid>
              </Grid>
            </Grid>
          )}
        </Grid>
        {description && <FormHelperText>{description}</FormHelperText>}
      </Stack>
    </Toolbar>
  );
});

export default ArrayLayoutToolbar;
