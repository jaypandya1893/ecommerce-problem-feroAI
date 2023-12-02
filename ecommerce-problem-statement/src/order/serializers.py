from rest_framework import serializers
from order.models import Order
from order_item.models import OrderItem
from order_item.serializers import OrderItemSerializer
from django.utils import timezone

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "order_number", "customer", "order_date", "address","order_items"]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        products = self.context['request'].query_params.get("products", None)

        if products:
            product_list = products.split(',')
            filtered_order_items = instance.order_items.filter(product__name__in=product_list)
            if filtered_order_items.exists():
                representation['order_items'] = OrderItemSerializer(filtered_order_items, many=True).data
                return representation
        return None
    
    def validate_order_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Order Date cannot be in the past.")
        return value
    
    def validate_order_items(self, data):
        """
        Validate the cumulative weight of the order.
        """
        cumulative_weight = sum(item['product'].weight * item['quantity'] for item in data if item['product'].weight is not None)
        if cumulative_weight > 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")

        return data
    
    def create(self, validated_data):
        order_item_data = validated_data.pop("order_items")
        order = Order.objects.create(**validated_data)

        for item_data in order_item_data:
            OrderItem.objects.create(order=order,**item_data)
        return order
    
    def update(self, instance, validated_data):
        order_item_data = validated_data.pop("order_items")
        orders=(instance.order_items).all()
        orders=list(orders)
        
        instance.order_date = validated_data.get("order_date", instance.order_date)
        instance.address = validated_data.get("address", instance.address)
        instance.customer = validated_data.get("customer", instance.customer)
        instance.save()

        for item_data in order_item_data:
            orderses=orders.pop(0)
            orderses.product = item_data.get("product",orderses.product)
            orderses.quantity = item_data.get("quantity",orderses.quantity)
            orderses.save()
        return instance