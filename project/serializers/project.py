from rest_framework import serializers

from hr.models import User
from constants import ProjectStatus
from project.models import Project
from project.serializers import MaterialSerializer


class ProjectSerializer(serializers.ModelSerializer):
    contractor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    status = serializers.ChoiceField(choices=ProjectStatus.choices, default=ProjectStatus.PENDING)
    materials = MaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
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
        read_only_fields = ["id", "start_date"]
