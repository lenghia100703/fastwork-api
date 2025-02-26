from django.db import models
from django.utils.text import slugify

from constants import ProjectStatus, Gender
from libs.models import BaseModel


class Project(BaseModel):
    customer_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    customer_gender = models.CharField(
        max_length=50,
        choices=Gender.choices,
    )
    customer_phone = models.CharField(max_length=20, blank=True, null=True)
    project_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        max_length=512, null=True, blank=True, db_index=True, unique=True
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
        blank=True,
        null=True,
    )
    total_cost = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        help_text="Tổng chi phí (VND)",
        blank=True,
        null=True,
    )
    paid_amount = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        blank=True,
        null=True,
    )
    debt_amount = models.DecimalField(
        max_digits=20,
        decimal_places=0,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.project_name

    def set_slug(self):
        self.slug = slugify(self.project_name)
        if Project.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = f"{self.slug}-{self.id}"

    def check_debt(self):
        return self.debt_amount > 0

    def save(self, *args, **kwargs):
        if not self.project_name and self.customer_name:
            project_name = ""
            if self.customer_gender == Gender.FEMALE:
                project_name = f"Công trình nhà bà {self.customer_name}"
            elif self.customer_gender == Gender.MALE:
                project_name = f"Công trình nhà ông {self.customer_name}"
            else:
                project_name = f"Công trình nhà {self.customer_name}"
            self.project_name = project_name
        self.set_slug()
        super().save(*args, **kwargs)
