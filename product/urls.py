from rest_framework import routers

from product.views import ProductViewSet

router = routers.DefaultRouter()

router.register(r"products", ProductViewSet, basename="products")


urlpatterns = router.urls
