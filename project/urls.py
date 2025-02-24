from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet, MaterialViewSet

router = DefaultRouter()
router.register(r"", ProjectViewSet)
router.register(r"materials", MaterialViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
