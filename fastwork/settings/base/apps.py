DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
EXTERNAL_APPS = [
    "anymail",
    "django_extensions",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "django_celery_beat",
    "django_celery_results",
    "drf_standardized_errors",
    "drf_spectacular",
    "ckeditor",
    "ckeditor_uploader",
]
INTERNAL_APPS = [
    "hr.apps.HrConfig",
    "project.apps.ProjectConfig",
]
INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS
