from .base import config_parser

GOOGLE_CLIENT_ID = config_parser.get("google", "CLIENT_ID", fallback="")
GOOGLE_CLIENT_SECRET = config_parser.get(
    "google", "CLIENT_SECRET", fallback=""
)
GOOGLE_REDIRECT_URI = config_parser.get("google", "REDIRECT_URI", fallback="")
