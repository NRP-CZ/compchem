from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    ".",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "experiments_search": "./js/experiments/search/index.js",
                "experiments_deposit_form": "./js/experiments/forms/index.js",
            },
            dependencies={
                # "react": "^18.2.0",
                # "react-dom": "^18.2.0",
                # "react-dropzone": "^14.2.3",
                # "react-router-dom": "^6.20.1",
                # "react-scripts": "5.0.1",

                "@emotion/react": "^11.11",
                "@emotion/styled": "^11.11",
                "@jsonforms/core": "^3.2",
                "@jsonforms/material-renderers": "^3.2",
                "@jsonforms/react": "^3.2",
                "@mui/icons-material": "^5.15",
                "@mui/lab": "^5.0.0-alpha.1",
                "@mui/material": "^5.15",
                "@mui/x-date-pickers": "",
                "ajv": "",
            },
            devDependencies={
                "typescript": "^4.4.3",
                "@types/react": "^18.0.0",
                "@types/react-dom": "^18.0.0",
            },
            aliases={},
        )
    },
)
