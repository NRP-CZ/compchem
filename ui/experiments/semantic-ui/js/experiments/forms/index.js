import { createFormAppInit, parseFormAppConfig } from "@js/oarepo_ui";
import FormFieldsContainer from "./FormFieldsContainer.jsx"
import CustomFieldsContainer from "./CustomFieldsContainer.jsx"

/** NOTE: This reads configuration for a form app present on a page
 *   In HTML/Jinja, represented by an element with a specific id
 *   (defaults to "form-app").
 *
 *   <div id="form-app" />
 */
const { formConfig } = parseFormAppConfig()

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
  // [`${overridableIdPrefix}.FormApp.layout`]: YourComponent,
  [`${overridableIdPrefix}.FormFields.container`]: FormFieldsContainer,     /* input fields */
  [`${overridableIdPrefix}.CustomFields.container`]: CustomFieldsContainer, /* idk */
  //[`${overridableIdPrefix}.Errors.container`]: FormFieldsContainer,         /* error display */
  //[`${overridableIdPrefix}.FormActions.container`]: FormFieldsContainer,    /* save draft, preview, publish buttons */
}


createFormAppInit({componentOverrides});

// invenio webpack clean create
// invenio webpack install --legacy-peer-deps
// invenio webpack build --production
