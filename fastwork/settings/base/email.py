from .anymail import SENDGRID_API_KEY, SENDGRID_EMAIL_SENDER
from .base import config_parser

EMAIL_SENDER = config_parser.get("email", "EMAIL_SENDER", fallback="")
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
if SENDGRID_API_KEY:
    EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
    EMAIL_SENDER = SENDGRID_EMAIL_SENDER
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = config_parser.get("email", "EMAIL_HOST", fallback="")
    EMAIL_PORT = config_parser.get("email", "EMAIL_PORT", fallback="")
    EMAIL_USE_TLS = config_parser.get("email", "EMAIL_USE_TLS", fallback="")
    EMAIL_HOST_USER = config_parser.get("email", "EMAIL_HOST_USER", fallback="")
    EMAIL_HOST_PASSWORD = config_parser.get("email", "EMAIL_HOST_PASSWORD", fallback="")

DEFAULT_FROM_EMAIL = EMAIL_SENDER
