import React, { useState, useCallback } from 'react';
import { Dialog, Button, DialogTitle, DialogContent, DialogContentText, DialogActions } from '@mui/material';


const useConfirmDialog = () => {
    const [open, setOpen] = useState(false);
    const [dialogProps, setDialogProps] = useState({});

    const showDialog = useCallback((title, message, onConfirm) => {
        setDialogProps({ title, message, onConfirm });
        setOpen(true);
    }, []);

    const handleClose = useCallback(() => {
        setOpen(false);
    }, []);

    const handleConfirm = useCallback(() => {
        setOpen(false);
        if (dialogProps.onConfirm)
            dialogProps.onConfirm();

    }, [dialogProps]);

    const ConfirmDialog = () => (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="alert-dialog-title"
            aria-describedby="alert-dialog-description"
        >
            <DialogTitle id="alert-dialog-title">{dialogProps.title}</DialogTitle>
            <DialogContent>
                <DialogContentText id="alert-dialog-description" style={{ whiteSpace: 'pre-line' }}>
                    {dialogProps.message}
                </DialogContentText>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleConfirm} color="primary" autoFocus>
                    Confirm
                </Button>
            </DialogActions>
        </Dialog>
    );

    return [showDialog, ConfirmDialog];
};

export default useConfirmDialog;
