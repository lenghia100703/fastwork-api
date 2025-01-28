from datetime import timedelta

from .base import config_parser

ACCESS_TOKEN_LIFETIME = config_parser.getint(
    "drf-simplejwt", "ACCESS_TOKEN_LIFETIME", fallback=60
)
REFRESH_TOKEN_LIFETIME = config_parser.getint(
    "drf-simplejwt", "REFRESH_TOKEN_LIFETIME", fallback=60
)


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=ACCESS_TOKEN_LIFETIME),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=REFRESH_TOKEN_LIFETIME),
}
