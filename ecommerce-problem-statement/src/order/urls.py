from django.urls import include, path
from order.views import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("orders", viewset=OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
]
