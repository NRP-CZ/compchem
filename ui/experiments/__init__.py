from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource


class ExperimentsResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/experiments/"
    blueprint_name = "experiments"
    ui_serializer_class = "experiments.resources.records.ui.ExperimentsUIJSONSerializer"
    api_service = "experiments"

    components = [BabelComponent]
    try:
        from oarepo_vocabularies.ui.resources.components import (
            DepositVocabularyOptionsComponent,
        )
        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    application_id="experiments"

    templates = {
        "detail": "experiments.Detail",
        "search": "experiments.Search",
        "edit": "experiments.Deposit",
        "create":"experiments.Deposit",
    }

    # def search_endpoint_url(self, identity, api_config, overrides={}, **kwargs):
    #     return f"/api/user{api_config.url_prefix}"


class ExperimentsResource(RecordsUIResource):
    pass


def create_blueprint(app):
    """Register blueprint for this resource."""
    return ExperimentsResource(ExperimentsResourceConfig()).as_blueprint()
