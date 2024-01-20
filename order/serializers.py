from rest_framework import serializers

from order.models import CartOrder, OrderProduct
from product.serializers import ProductSerializer, IngredientSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = OrderProduct
        fields = [
            "order_id",
            "product",
            "product_quantity",
            "ingredients",
        ]


class CartOrderSerializer(serializers.ModelSerializer):
    cart = OrderProductSerializer(many=True)

    class Meta:
        model = CartOrder
        fields = [
            "name",
            "status",
            "total_price",
            "phone",
            "email",
            "receiving",
            "comment",
            "promo_code",
            "billing",
            "street",
            "building",
            "apartment",
            "created_at",
            "cart",
        ]

    def create(self, validated_data):
        cart_data = validated_data.pop("cart")
        order = CartOrder.objects.create(**validated_data)
        print(order)

        for item_data in cart_data:
            ingredients_data = item_data.pop("ingredients", [])
            order_product = OrderProduct.objects.create(order_id=order.id, **item_data)
            print(order_product)

            order_product.ingredients.set(ingredients_data)

        return order
