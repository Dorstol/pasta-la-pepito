from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from product.models import Product, Ingredient

STATUS = (
    ("PENDING", "Pending"),
    ("CONFIRMED", "Confirmed"),
    ("DELIVERED", "Delivered"),
    ("CANCELED", "Canceled"),
)

RECEIVING = (
    ("DELIVERY", "Delivery"),
    ("SELF_PICKUP", "Self pickup"),
)

BILLING = (
    ("CREDIT_CARD", "Credit card"),
    ("CASH", "Cash"),
)


class CustomerOrder(models.Model):
    name = models.CharField(
        max_length=255,
    )
    status = models.CharField(
        choices=STATUS,
        default=STATUS[0],
        max_length=20,
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    phone = PhoneNumberField(
        region="UA",
    )
    email = models.EmailField()
    receiving = models.CharField(
        choices=RECEIVING,
        default=RECEIVING[0],
        max_length=20,
    )
    comment = models.TextField(
        blank=True,
        null=True,
    )
    promo_code = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    billing = models.CharField(
        choices=BILLING,
        max_length=20,
    )
    street = models.CharField(
        max_length=255,
    )
    building = models.CharField(
        max_length=255,
    )
    apartment = models.CharField(
        max_length=255,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
    )
    cart = models.ManyToManyField(
        "OrderProduct",
        related_name="orders",
    )

    def get_full_address(self):
        return f"{self.street} Vul., bld. {self.building}, apt. {self.apartment}"


class OrderProduct(models.Model):
    order = models.ForeignKey(
        CustomerOrder,
        on_delete=models.CASCADE,
        related_name="order_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="order_products",
    )
    quantity = models.IntegerField(
        default=1,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="order_products",
        blank=True,
    )

    def __str__(self):
        return f"Order: {self.order.name}, Product: {self.product.name}, Quantity: {self.quantity}"
