from django.db import models

from libs.models import BaseModel


class Material(BaseModel):
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        related_name="materials",
    )
    unit_price = models.DecimalField(
        max_digits=20,
        decimal_places=0,
    )
    total_price = models.DecimalField(
        max_digits=20,
        decimal_places=0,
    )
    purchased_date = models.DateTimeField(auto_now_add=True)
