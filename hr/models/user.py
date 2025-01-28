from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from constants import UserRole
from libs.models import BaseModel


class User(BaseModel, AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    email_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=255,
        choices=UserRole.choices,
        default=UserRole.WORKER,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users/avatars", null=True, blank=True
    )
    address = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return f"#{self.id} {self.username}"

    def get_display_name(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
