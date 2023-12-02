from django.urls import include, path


app_name = "api"

urlpatterns = [
    path("", include("customer.urls"), name="custometapi"),
    path("", include("order.urls"), name="orderapi"),
    path("", include("product.urls"), name="productapi"),
    path("", include("order_item.urls"), name="orderitemapi"),
]
