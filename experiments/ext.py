import re
from functools import cached_property

from oarepo_requests.proxies import current_oarepo_requests_service
from oarepo_requests.resources.draft.config import DraftRecordRequestsResourceConfig
from oarepo_requests.resources.draft.types.config import DraftRequestTypesResourceConfig

from experiments import config


class ExperimentsExt:

    def __init__(self, app=None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.app = app

        self.init_config(app)
        if not self.is_inherited():
            self.register_flask_extension(app)

    def register_flask_extension(self, app):

        app.extensions["experiments"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_0-9]*$", identifier) and not identifier.startswith("_"):
                if isinstance(app.config.get(identifier), list):
                    app.config[identifier] += getattr(config, identifier)
                elif isinstance(app.config.get(identifier), dict):
                    for k, v in getattr(config, identifier).items():
                        if k not in app.config[identifier]:
                            app.config[identifier][k] = v
                else:
                    app.config.setdefault(identifier, getattr(config, identifier))

    def is_inherited(self):
        from importlib_metadata import entry_points

        ext_class = type(self)
        for ep in entry_points(group="invenio_base.apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        for ep in entry_points(group="invenio_base.api_apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        return False

    @cached_property
    def service_records(self):
        service_config = config.EXPERIMENTS_RECORD_SERVICE_CONFIG
        if hasattr(service_config, "build"):
            config_class = service_config.build(self.app)
        else:
            config_class = service_config()

        service_kwargs = {"config": config_class}
        return config.EXPERIMENTS_RECORD_SERVICE_CLASS(
            **service_kwargs,
            files_service=self.service_files,
            draft_files_service=self.service_draft_files,
        )

    @cached_property
    def resource_records(self):
        return config.EXPERIMENTS_RECORD_RESOURCE_CLASS(
            service=self.service_records,
            config=config.EXPERIMENTS_RECORD_RESOURCE_CONFIG(),
        )

    @cached_property
    def service_record_requests(self):
        return config.EXPERIMENTS_REQUESTS_SERVICE_CLASS(
            record_service=self.service_records,
            oarepo_requests_service=current_oarepo_requests_service,
        )

    @cached_property
    def resource_record_requests(self):
        return config.EXPERIMENTS_REQUESTS_RESOURCE_CLASS(
            service=self.service_record_requests,
            config=config.EXPERIMENTS_RECORD_RESOURCE_CONFIG(),
            record_requests_config=DraftRecordRequestsResourceConfig(),
        )

    @cached_property
    def service_record_request_types(self):
        return config.EXPERIMENTS_REQUEST_TYPES_SERVICE_CLASS(
            record_service=self.service_records,
            oarepo_requests_service=current_oarepo_requests_service,
        )

    @cached_property
    def resource_record_request_types(self):
        return config.EXPERIMENTS_REQUEST_TYPES_RESOURCE_CLASS(
            service=self.service_record_request_types,
            config=config.EXPERIMENTS_RECORD_RESOURCE_CONFIG(),
            record_requests_config=DraftRequestTypesResourceConfig(),
        )

    @cached_property
    def published_service_records(self):
        from experiments.services.records.published.config import (
            ExperimentsPublishedServiceConfig,
        )
        from experiments.services.records.published.service import (
            ExperimentsPublishedService,
        )

        return ExperimentsPublishedService(
            config=ExperimentsPublishedServiceConfig(
                proxied_drafts_config=self.service_records.config
            ),
        )

    @cached_property
    def service_files(self):
        service_config = config.EXPERIMENTS_FILES_SERVICE_CONFIG
        if hasattr(service_config, "build"):
            config_class = service_config.build(self.app)
        else:
            config_class = service_config()

        service_kwargs = {"config": config_class}
        return config.EXPERIMENTS_FILES_SERVICE_CLASS(
            **service_kwargs,
        )

    @cached_property
    def resource_files(self):
        return config.EXPERIMENTS_FILES_RESOURCE_CLASS(
            service=self.service_files,
            config=config.EXPERIMENTS_FILES_RESOURCE_CONFIG(),
        )

    @cached_property
    def published_service_files(self):
        from experiments.services.files.published.config import (
            ExperimentsFilePublishedServiceConfig,
        )
        from experiments.services.files.published.service import (
            ExperimentsFilePublishedService,
        )

        return ExperimentsFilePublishedService(
            config=ExperimentsFilePublishedServiceConfig(),
        )

    @cached_property
    def service_draft_files(self):
        service_config = config.EXPERIMENTS_DRAFT_FILES_SERVICE_CONFIG
        if hasattr(service_config, "build"):
            config_class = service_config.build(self.app)
        else:
            config_class = service_config()

        service_kwargs = {"config": config_class}
        return config.EXPERIMENTS_DRAFT_FILES_SERVICE_CLASS(
            **service_kwargs,
        )

    @cached_property
    def resource_draft_files(self):
        return config.EXPERIMENTS_DRAFT_FILES_RESOURCE_CLASS(
            service=self.service_draft_files,
            config=config.EXPERIMENTS_DRAFT_FILES_RESOURCE_CONFIG(),
        )
