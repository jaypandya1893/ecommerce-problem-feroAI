from django.db import models
from django.core.validators import RegexValidator
from custom.custommodel import CustomModel


# Create your models here.
class Customer(CustomModel):
    name=models.CharField(max_length=100, blank=True,null=True)
    contact_number = models.CharField(max_length=13,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
   

    def __str__(self):
        return self.name


