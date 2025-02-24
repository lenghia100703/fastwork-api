from rest_framework import serializers

from project.models import Project
from project.models import Material


class MaterialSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Material
        fields = [
            "id",
            "name",
            "quantity",
            "project",
            "unit_price",
            "total_price",
            "purchased_date",
        ]
        read_only_fields = ["id", "purchased_date"]
