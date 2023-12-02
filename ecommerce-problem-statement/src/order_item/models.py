from django.db import models
from custom.custommodel import CustomModel
from order.models import Order
from product.models import Product


# Create your models here.
class OrderItem(CustomModel):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items",null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.order.order_number


