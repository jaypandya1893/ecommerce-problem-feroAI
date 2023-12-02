from django.urls import include, path
from customer.views import CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("customers", viewset=CustomerViewSet, basename="customers")

urlpatterns = [
    path("", include(router.urls)),
]
