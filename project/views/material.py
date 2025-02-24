from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from project.filters import MaterialFilter
from project.models import Material
from project.serializers import MaterialSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = MaterialFilter

    def get_queryset(self):
        project_id = self.request.query_params.get("project_id")
        if project_id:
            return self.queryset.filter(project_id=project_id)
        return self.queryset