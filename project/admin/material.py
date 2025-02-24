from django.contrib import admin

from project.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass
