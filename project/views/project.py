from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from project.filters import ProjectFilter
from project.models import Project
from project.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_class = ProjectFilter

    def perform_create(self, serializer):
        if not serializer.validated_data.get("contractor"):
            serializer.save(contractor=self.request.user)
        else:
            serializer.save()
