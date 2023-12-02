from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name", "weight"]
    
    def validate_name(self, value):
        """
        Validate that the 'name' field is unique.
        """
        existing_product = Product.objects.filter(name=value).exclude(id=self.instance.id if self.instance else None).first()

        if existing_product:
            raise serializers.ValidationError("Product with this name already exists.")
        
        return value

    def validate_weight(self, value):
        """
        Validate that the 'weight' is a positive decimal and not more than 25kg.
        """
        if value is not None:
            if value <= 0:
                raise serializers.ValidationError("Weight must be a positive decimal value.")
            if value > 25:
                raise serializers.ValidationError("Weight must not be more than 25kg.")
        return value