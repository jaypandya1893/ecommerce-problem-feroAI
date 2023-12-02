from django.shortcuts import render
from django.db.models import Prefetch
from order_item.models import OrderItem
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ["id", "order_number", "customer__name", "order_date", "address", "order_items__product__name"]
    filterset_fields = ["customer__name", "order_items__product__name"]

    
    def get_queryset(self):
        queryset = super().get_queryset()
        customers = self.request.query_params.get("customer", None)

        if customers:
            customer_list = customers.split(',')
            queryset = queryset.filter(customer__name__in=customer_list)            
        return queryset
