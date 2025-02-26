import django_filters
from django_filters import OrderingFilter

from constants import ProjectStatus
from project.models import Project


class ProjectFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(field_name="customer_name", lookup_expr="icontains")
    address = django_filters.CharFilter(field_name="address", lookup_expr="icontains")
    status = django_filters.ChoiceFilter(field_name="status", choices=ProjectStatus.choices)
    start_date = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    contractor = django_filters.NumberFilter(field_name="contractor__id")
    has_debt = django_filters.CharFilter(method="filter_has_debt")

    o = OrderingFilter(
        fields=(
            ("customer_name", "customer_name"),
            ("start_date", "start_date"),
        ),
    )

    class Meta:
        model = Project
        fields = [
            "customer_name",
            "status",
            "address",
            "start_date",
            "contractor",
            "has_debt",
        ]

    @staticmethod
    def filter_has_debt(self, queryset, name, value):
        breakpoint()
        has_debt = value == "true"
        if has_debt:
            return queryset.filter(debt_amount__gt=0)
        return queryset.filter(debt_amount=0)
