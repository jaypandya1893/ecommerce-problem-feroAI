from django.urls import include, path
from product.views import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("products", viewset=ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
