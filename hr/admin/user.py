from django.contrib import admin

from ..models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "phone_number")
    list_filter = ("role",)
    search_fields = ("email", "phone_number")
