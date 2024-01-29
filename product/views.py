from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from product.models import Product, Category, Ingredient
from product.serializers import (
    ProductReadSerializer,
    ProductWriteSerializer,
    CategorySerializer,
    IngredientSerializer,
)


class ProductViewSet(ModelViewSet):
    """
    CRUD for product
    """

    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return ProductWriteSerializer

        return ProductReadSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    """
    List and Retrieve categories
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


class IngredientViewSet(ReadOnlyModelViewSet):
    """
    List ingredients
    """

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
