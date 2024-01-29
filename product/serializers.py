from rest_framework import serializers

from product.models import Product, Ingredient, Category


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer class for ingredients
    """

    class Meta:
        model = Ingredient
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for categories
    """

    class Meta:
        model = Category
        fields = "__all__"


class ProductReadSerializer(serializers.ModelSerializer):
    """
    Serializer class for read products
    """

    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductWriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for CRUD product
    """

    category = CategorySerializer()

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "short_description",
            "category",
            "rating",
        ]

    def create(self, validated_data):
        category = validated_data.pop("category")
        instance, created = Category.objects.get_or_create(**category)
        product = Product.objects.create(**validated_data, category=instance)

        return product
