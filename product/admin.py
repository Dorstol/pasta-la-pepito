from django.contrib import admin

from product.models import Product, Category, Ingredient


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "description",
        "short_description",
        "category",
        "image",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "short_description",
        "image",
    ]
