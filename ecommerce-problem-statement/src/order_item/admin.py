from django.contrib import admin
from .models import OrderItem


# Register your models here.
@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = [
        "id", "order", "product","quantity"
    ]