from django.shortcuts import render
from .models import OrderItem
from .serializers import OrderItemSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["id", "order_number", "customer__name", "order_date", "address", "orderitem__product__name"]
    filterset_fields = ["customer__name", "orderitem__product__name"]

    def get_queryset(self):
        queryset = super().get_queryset()
        products = self.request.query_params.get("products", None)
        customer_name = self.request.query_params.get("customer", None)

        if products: 
            queryset = queryset.filter(orderitem__product__name__in=products.split(','))

        if customer_name:
            queryset = queryset.filter(customer__name=customer_name)

        return queryset
