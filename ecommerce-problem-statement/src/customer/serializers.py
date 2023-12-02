from rest_framework import serializers
from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
        "id", "name", "contact_number","email"
    ]

    def validate_name(self, value):
        """
        Validate that the 'name' field is unique.
        """
        existing_customer = Customer.objects.filter(name=value).exclude(id=self.instance.id if self.instance else None).first()

        if existing_customer:
            raise serializers.ValidationError("Customer with this name already exists.")
        
        return value