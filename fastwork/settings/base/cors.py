from .base import config_parser

CORS_ALLOW_METHODS = []
try:
    _methods = config_parser.get("system", "CORS_ALLOW_METHODS", fallback="")
    if _methods:
        CORS_ALLOW_METHODS = [
            method for method in _methods.split(",") if method
        ]
except Exception:
    pass


CORS_ALLOWED_ORIGINS = []
try:
    _origins = config_parser.get("system", "CORS_ALLOWED_ORIGINS", fallback="")
    if _origins:
        CORS_ALLOWED_ORIGINS = [
            origin for origin in _origins.split(",") if origin
        ]
except Exception:
    pass
