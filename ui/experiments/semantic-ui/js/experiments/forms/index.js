import React from "react";
import { createFormAppInit, parseFormAppConfig } from "@js/oarepo_ui";
import { ThemeProvider } from '@mui/material/styles';

import FormFieldsContainer from "./FormFieldsContainer"
import CustomFieldsContainer from "./CustomFieldsContainer"
import FormActionsContainer from "./FormActionsContainer"
import { FormContextProvider } from "./context";
import theme from './theme';

/** NOTE: This reads configuration for a form app present on a page
 *   In HTML/Jinja, represented by an element with a specific id
 *   (defaults to "form-app").
 *
 *   <div id="form-app" />
 */
const { rootEl, record, formConfig, recordPermissions, files, links } = parseFormAppConfig()

console.log("files", files)

// set up record community
const params = new URLSearchParams(window.location.search);
const community = params.get('community');
const recordCommunity = record?.parent?.communities?.default || "";

if (community !== null && recordCommunity === "") {
    if (!record.parent)
        record.parent = {};
    if (!record.parent.communities)
        record.parent.communities = {};

    record.parent.communities.default = community;

    console.log("Setting record community to", community);
}


/** NOTE: To customize components in a specific form app instance,
 *   you need to obtain its `overridableIdPrefix` from the corresponding config first
 */
const { overridableIdPrefix } = formConfig

/*
export const overridableComponentIds = [
    "Errors.container",
    "FormActions.container",
    "FormApp.layout",
    "FormFields.container",
    "CustomFields.container",
];
*/

export const componentOverrides = {
    /** NOTE: Then you can then replace any existing ui
     * component with your own implementation, e.g.:
     */
    // [`${overridableIdPrefix}.FormApp.layout`]: FormAppLayout,                   /* main layout */
    // [`${overridableIdPrefix}.Errors.container`]: FormFieldsContainer,           /* error display */
    [`${overridableIdPrefix}.FormFields.container`]: FormFieldsContainer,       /* input fields */
    [`${overridableIdPrefix}.FormActions.container`]: FormActionsContainer,     /* save, preview, publish, delete buttons */
    // [`${overridableIdPrefix}.CustomFields.container`]: CustomFieldsContainer,   /* useless container (maybe use for Mol*?) */
}


const ContainerComponent = ({children}) => {
    return (
        <ThemeProvider theme={theme}>
            <FormContextProvider initialRecord={record}>
                {children}
            </FormContextProvider>
        </ThemeProvider>
    )
}

createFormAppInit({componentOverrides, ContainerComponent});
