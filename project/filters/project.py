import django_filters

from constants import ProjectStatus
from project.models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    status = django_filters.CharFilter(choices=ProjectStatus.choices)
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    contractor = django_filters.NumberFilter(field_name="contractor__id")

    class Meta:
        model = Project
        fields = [
            "name",
            "status",
            "start_date",
            "contractor",
        ]
