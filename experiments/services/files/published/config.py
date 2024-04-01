from experiments.services.files.config import ExperimentsFileServiceConfig


class ExperimentsFilePublishedServiceConfig(ExperimentsFileServiceConfig):
    service_id = "published_experiments_file"

    @property
    def components(self):
        return [*super().components]
