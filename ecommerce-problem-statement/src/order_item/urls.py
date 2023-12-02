from django.urls import include, path
from order_item.views import OrderItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("order-items", viewset=OrderItemViewSet, basename="order_items")

urlpatterns = [
    path("", include(router.urls)),
]
