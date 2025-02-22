from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from hr.models import User
from hr.serializers import UserSerializer


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    allowed_methods = ["get", "put", "patch", "delete"]
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=["get"], url_path="me", url_name="me")
    def get_me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.mark_deleted()
