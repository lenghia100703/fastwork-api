from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_admin_url(self):
        app_label = self._meta.app_label
        model_name = self._meta.model_name
        return f"/admin/{app_label}/{model_name}/{self.pk}/change/"

    @property
    def activity_display(self):
        if hasattr(self, "name"):
            return f"{self._meta.verbose_name} {self.name}"
        return f"{self._meta.verbose_name} #{self.pk}"
