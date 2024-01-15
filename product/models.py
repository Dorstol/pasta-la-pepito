from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        max_length=255,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    short_description = models.CharField(
        max_length=255,
    )
    image = models.ImageField(
        upload_to="ingredients/",
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=255,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    image = models.ImageField(
        upload_to="products/",
    )
    description = models.TextField()
    short_description = models.CharField(
        max_length=255,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        related_name="categories",
    )

    def __str__(self):
        return self.name
