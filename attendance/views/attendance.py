from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from attendance.filters import AttendanceFilter
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all().order_by('created_at')
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AttendanceFilter
    lookup_field = "id"
