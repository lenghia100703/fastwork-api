from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    SignUpAPIView,
    SignUpConfirmAPIView,
    LogoutAPIView,
    LoginAPIView,
    UserRefreshTokenAPIView,
    UserViewSet,
)

app_name = "hr"

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path(
        "login/refresh/",
        UserRefreshTokenAPIView.as_view(),
        name="login-refresh",
    ),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path(
        "signup/",
        SignUpAPIView.as_view(),
        name="signup",
    ),
    path(
        "signup/confirm/",
        SignUpConfirmAPIView.as_view(),
        name="signup-confirm",
    ),
]

default_router = DefaultRouter()
default_router.register("users", UserViewSet, basename="users")

urlpatterns += default_router.urls
