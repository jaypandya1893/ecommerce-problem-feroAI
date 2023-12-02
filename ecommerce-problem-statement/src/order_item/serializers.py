from rest_framework import serializers
from order_item.models import OrderItem
from django.utils import timezone

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields =[
        "id","order","product","quantity"
    ]