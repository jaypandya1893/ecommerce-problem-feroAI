from django.db import models
from custom.custommodel import CustomModel
from customer.models import Customer


# Create your models here.
class Order(CustomModel):
    order_number = models.CharField(max_length=10,null=True, blank=True, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers")
    order_date=models.DateField()
    address=models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.order_number
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            latest_order = Order.objects.filter(order_number__startswith='ORD').order_by('-order_number').first()
            if latest_order:
                last_number = int(latest_order.order_number[3:])
                new_number = f'{last_number + 1:05d}'
            else:
                new_number = '00001'
            self.order_number = f'ORD{new_number}'
        super().save(*args, **kwargs)




