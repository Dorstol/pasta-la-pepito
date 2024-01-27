from django.contrib import admin

from order.models import CustomerOrder, OrderProduct


@admin.register(CustomerOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "status",
        "total_price",
        "phone",
        "receiving",
        "billing",
        "comment",
        "promo_code",
        "get_full_address",
    ]


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "quantity",
        "display_ingredients",
    ]

    def display_ingredients(self, obj):
        return ", ".join([ingredient.name for ingredient in obj.ingredients.all()])

    display_ingredients.short_description = "Ingredients"
