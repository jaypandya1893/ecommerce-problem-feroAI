from django.db import models


class CustomModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)
    Updated_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
