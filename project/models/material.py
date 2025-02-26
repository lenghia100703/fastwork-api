from django.db import models
from django.utils.text import slugify

from libs.models import BaseModel


class Material(BaseModel):
    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=512,
        blank=True,
        null=True,
        unique=True,
        db_index=True,
    )
    quantity = models.PositiveIntegerField(
        default=1,
        blank=True,
        null=True,
    )
    unit = models.CharField(
        max_length=150,
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

    def __str__(self):
        return self.name

    def set_slug(self):
        if not self.slug:
            self.slug = slugify(self.name)
        if Material.objects.filter(slug=self.slug).exclude(pk=self.id).exists():
            self.slug = f"{self.slug}-{self.id}"

    def save(self, *args, **kwargs):
        self.unit = self.unit.lower()
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
