from flask import current_app
from werkzeug.local import LocalProxy


def _ext_proxy(attr):
    return LocalProxy(lambda: getattr(current_app.extensions["experiments"], attr))


current_service = _ext_proxy("service_records")
current_published_service = _ext_proxy("published_service_records")
current_files_published_service = _ext_proxy("published_service_files")
"""Proxy to the instantiated service."""
"""Proxy to the instantiated vocabulary service."""


current_resource = _ext_proxy("resource_records")
"""Proxy to the instantiated resource."""
