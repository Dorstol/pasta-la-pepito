from django.contrib import admin

from order.models import Order, OrderProduct


@admin.register(Order)
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
        "product_quantity",
        "ingredients",
    ]
