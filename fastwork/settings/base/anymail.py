from .base import config_parser

SENDGRID_API_KEY = config_parser.get(
    "anymail", "SENDGRID_API_KEY", fallback=""
)
SENDGRID_EMAIL_SENDER = config_parser.get(
    "anymail", "SENDGRID_EMAIL_SENDER", fallback=""
)

ANYMAIL = {
    "SENDGRID_API_KEY": SENDGRID_API_KEY,
}
