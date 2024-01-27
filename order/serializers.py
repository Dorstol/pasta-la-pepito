from rest_framework import serializers

from order.models import CustomerOrder, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["product", "quantity", "ingredients"]


class CustomerOrderSerializer(serializers.ModelSerializer):
    cart = OrderProductSerializer(many=True)

    class Meta:
        model = CustomerOrder
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
            "cart",
        ]

    def create(self, validated_data):
        order_products_data = validated_data.pop("cart")
        order = CustomerOrder.objects.create(**validated_data)

        for order_product_data in order_products_data:
            ingredients_data = order_product_data.pop("ingredients", [])
            order_product = OrderProduct.objects.create(
                order=order, **order_product_data
            )
            order_product.ingredients.set(ingredients_data)

        return order
