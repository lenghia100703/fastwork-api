[system]
DEBUG=true
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URL=postgres://fastwork:password@localhost:5432/fastwork
#DATABASE_URL=sqlite:///db.sqlite3  # or use sqlite3 to quickly setup development environment

SENTRY_DSN=YOUR_SENTRY_DSN
SENTRY_TRACES_SAMPLE_RATE=0.3
SENTRY_SAMPLE_RATE=0.5

CSRF_TRUSTED_ORIGINS=  # a list of origins seperated by commas

[celery]
BROKER_URL=redis://localhost:6379/0
TASK_ALWAYS_EAGER=True
TASK_EAGER_PROPAGATES=True

[cache]
URL=redis://localhost:6379/0
PREFIX=
TIMEOUT=2592000

[drf-simplejwt]
ACCESS_TOKEN_LIFETIME=<INT> # in minutes
REFRESH_TOKEN_LIFETIME=<INT> # in days

[google]
CLIENT_ID=
CLIENT_SECRET=
REDIRECT_URI=
PROJECT_ID=

[anymail]
SENDGRID_API_KEY=YOUR_API_KEY
SENDGRID_EMAIL_SENDER=YOUR_EMAIL_SENDER


[email]
EMAIL_SENDER=YOUR_EMAIL
STATIC_DOMAIN_FOR_EMAIL=http://localhost:8000
