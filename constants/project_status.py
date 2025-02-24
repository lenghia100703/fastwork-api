from django.db import models
from django.utils.translation import gettext_lazy as _


class ProjectStatus(models.TextChoices):
    PROGRESS = "progress", _("Progress")
    DONE = "done", _("Done")
    PENDING = "pending", _("Pending")
