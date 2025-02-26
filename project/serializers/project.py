from rest_framework import serializers

from hr.models import User
from constants import ProjectStatus
from libs.validators import PhoneNumberValidator
from project.models import Project
from project.serializers import MaterialSerializer


class ProjectSerializer(serializers.ModelSerializer):
    contractor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    status = serializers.ChoiceField(choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    materials = MaterialSerializer(many=True, read_only=True)
    customer_phone = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        max_length=20,
        required=False,
        validators=[PhoneNumberValidator()],
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "customer_name",
            "customer_phone",
            "customer_gender",
            "project_name",
            "slug",
            "address",
            "notes",
            "contractor",
            "start_date",
            "estimate_end_date",
            "status",
            "total_estimated_cost",
            "total_cost",
            "paid_amount",
            "debt_amount",
            "materials",
        ]
        read_only_fields = ["id", "start_date", "slug"]
