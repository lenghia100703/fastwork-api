import os

from .base import BASE_DIR

# 3 files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles")

STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static"),)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

CKEDITOR_UPLOAD_PATH = "media/images/post/"
