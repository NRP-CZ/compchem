import re
from functools import cached_property

from oarepo_requests.proxies import current_oarepo_requests_service
from oarepo_requests.resources.draft.config import DraftRecordRequestsResourceConfig

from experiments import config


class ExperimentsExt:

    def __init__(self, app=None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""

        self.init_config(app)
        if not self.is_inherited():
            self.register_flask_extension(app)

    def register_flask_extension(self, app):

        app.extensions["experiments"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_0-9]*$", identifier) and not identifier.startswith("_"):
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
        return config.EXPERIMENTS_RECORD_SERVICE_CLASS(
            config=config.EXPERIMENTS_RECORD_SERVICE_CONFIG(),
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
    def service_requests(self):
        return config.EXPERIMENTS_REQUESTS_SERVICE_CLASS(
            record_service=self.service_records,
            oarepo_requests_service=current_oarepo_requests_service,
        )

    @cached_property
    def resource_requests(self):
        return config.EXPERIMENTS_REQUESTS_RESOURCE_CLASS(
            service=self.service_requests,
            config=config.EXPERIMENTS_RECORD_RESOURCE_CONFIG(),
            record_requests_config=DraftRecordRequestsResourceConfig(),
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
        return config.EXPERIMENTS_FILES_SERVICE_CLASS(
            config=config.EXPERIMENTS_FILES_SERVICE_CONFIG(),
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
        return config.EXPERIMENTS_DRAFT_FILES_SERVICE_CLASS(
            config=config.EXPERIMENTS_DRAFT_FILES_SERVICE_CONFIG(),
        )

    @cached_property
    def resource_draft_files(self):
        return config.EXPERIMENTS_DRAFT_FILES_RESOURCE_CLASS(
            service=self.service_draft_files,
            config=config.EXPERIMENTS_DRAFT_FILES_RESOURCE_CONFIG(),
        )
