from django.db import models
from django.utils.translation import gettext_lazy as _


class Shift(models.TextChoices):
    MORNING = "morning", _("Morning")
    AFTERNOON = "afternoon", _("Afternoon")
    NIGHT = "night", _("Night")
