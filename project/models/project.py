from django.db import models

from libs.models import BaseModel
from constants import ProjectStatus


class Project(BaseModel):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    address = models.TextField(
        blank=True,
        null=True,
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )
    contractor = models.ForeignKey(
        "hr.User",
        on_delete=models.CASCADE,
        related_name="projects",
    )
    start_date = models.DateTimeField(auto_now_add=True)
    estimate_end_date = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING,
        blank=True,
        null=True,
    )
    total_estimated_cost = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        help_text="Chi phí dự kiến (VND)",
    )
    total_cost = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        help_text="Tổng chi phí (VND)",
    )
    paid_amount = models.DecimalField(
        max_digits=20,
        decimal_places=0,
    )
    debt_amount = models.DecimalField(
        max_digits=20,
        decimal_places=0,
    )