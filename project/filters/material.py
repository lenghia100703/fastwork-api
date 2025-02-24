import django_filters

from project.models import Material


class MaterialFilter(django_filters.FilterSet):
    project = django_filters.NumberFilter(field_name="project__id")
    name = django_filters.CharFilter(lookup_expr="icontains")
    purchased_date = django_filters.DateFilter(field_name="purchased_date", lookup_expr="gte")

    class Meta:
        model = Material
        fields = [
            "name",
            "project",
            "purchased_date",
        ]
