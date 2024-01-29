from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import ProductViewSet, CategoryViewSet, IngredientViewSet

app_name = "products"

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"ingredients", IngredientViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
