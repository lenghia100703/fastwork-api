"""
    This configuration file overrides some necessary configs
    to easily develop the app.
"""

from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE


INSTALLED_APPS += [
    "debug_toolbar",
    "corsheaders",
]

# Ref: https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware"
]
INTERNAL_IPS = ["127.0.0.1"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
