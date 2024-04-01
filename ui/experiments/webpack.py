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
            dependencies={},
            devDependencies={},
            aliases={},
        )
    },
)
