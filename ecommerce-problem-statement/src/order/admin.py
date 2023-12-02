from django.contrib import admin
from .models import Order


# Register your models here.
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [
        "id", "order_number", "customer","order_date","address"
    ]