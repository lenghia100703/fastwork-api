from django.db import models

from constants import AttendanceStatus, UserRole
from constants.shift import Shift
from libs.models import BaseModel


class Attendance(BaseModel):
    worker = models.ForeignKey(
        "hr.User",
        on_delete=models.CASCADE,
        related_name="attendances",
    )
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        related_name="attendances",
    )
    status = models.CharField(
        max_length=50,
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.PENDING,
    )
    shift = models.CharField(
        max_length=50,
        choices=Shift.choices,
    )

    def __str__(self):
        return f"{self.worker} - {self.project}"

    def save(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        if user and user.role == UserRole.CONTRACTOR:
            self.status = AttendanceStatus.CONFIRMED
        super().save(*args, **kwargs)
