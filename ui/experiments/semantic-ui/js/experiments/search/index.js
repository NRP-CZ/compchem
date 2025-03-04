import {
  // parseSearchAppConfigs,
  createSearchAppsInit,
} from "@js/oarepo_ui";

/** NOTE: This reads configs for any search app present on a page
 *   In HTML/Jinja, a single search app instance is typically represented
 *   as a div with a config data attribute:
 *
 *   <div data-invenio-search-config='...' />
 */
// const [searchAppConfig, ...otherSearchAppConfigs] = parseSearchAppConfigs()

/** NOTE: To customize components in a specific search app instance,
 *   you need to obtain its `overridableIdPrefix` from the corresponding config first
 */
// const { overridableIdPrefix } = searchAppConfig

/*
export const overridableComponentIds = [
  "ActiveFilters.element",
  "AutocompleteSearchBar.element",
  "BucketAggregation.element",
  "BucketAggregationContainer.element",
  "BucketAggregationValues.element",
  "Count.Element",
  "Error.element",
  "Pagination.element",
  "ResultsGrid.container",
  "ResultsGrid.item",
  "ResultsList.container",
  "ResultsList.item",
  "ResultsLoader.element",
  "ResultsMultiLayout.element",
  "ResultsPerPage.element",
  "SearchApp.facets",
  "SearchApp.layout",
  "SearchApp.resultOptions",
  "SearchApp.results",
  "SearchApp.resultsPane",
  "SearchApp.searchbar",
  "SearchBar.element",
  "SearchFilters.Toggle.element",
  "SearchHelpLinks",
  "Sort.element",
  "SortBy.element",
  "SortOrder.element",
  "SearchApp.buttonSidebarContainer",
];
*/


export const componentOverrides = {
  /** NOTE: Then you can then replace any existing search ui
   * component with your own implementation, e.g.:
   */
  // [`${overridableIdPrefix}.AutocompleteSearchBar.element`]: YourComponent,       // https://github.com/inveniosoftware/react-searchkit/blob/master/src/lib/components/AutocompleteSearchBar/AutocompleteSearchBar.js#L117-L140
};

createSearchAppsInit({ componentOverrides });
