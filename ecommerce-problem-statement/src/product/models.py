from django.db import models
from custom.custommodel import CustomModel
# Create your models here.
class Product(CustomModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=3,null=True, blank=True)

    def __str__(self):
        return self.name