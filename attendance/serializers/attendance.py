from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from constants import AttendanceStatus
from constants.shift import Shift
from hr.models import User
from project.models import Project
from ..models import Attendance


class AttendanceSerializer(ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    status = serializers.ChoiceField(
        choices=AttendanceStatus.choices,
        default=AttendanceStatus.PENDING,
    )
    shift = serializers.ChoiceField(
        choices=Shift.choices,
    )

    class Meta:
        model = Attendance
        fields = [
            "worker",
            "project",
            "status",
            "shift",
        ]
