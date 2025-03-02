import django_filters
from django_filters import OrderingFilter

from attendance.models import Attendance
from constants import AttendanceStatus
from constants.shift import Shift


class AttendanceFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(field_name="status", choices=AttendanceStatus.choices)
    shift = django_filters.ChoiceFilter(field_name="shift", choices=Shift.choices)
    created_at = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    worker = django_filters.NumberFilter(field_name="worker__id")
    project = django_filters.NumberFilter(field_name="worker__id")

    o = OrderingFilter(
        fields=(
            ("created_at", "created_at"),
        ),
    )

    class Meta:
        model = Attendance
        fields = [
            "status",
            "shift",
            "created_at",
            "worker",
            "project",
        ]
