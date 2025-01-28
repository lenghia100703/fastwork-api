from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    WORKER = "worker", _("Worker")
    CONTRACTOR = "contractor", _("Contractor")
