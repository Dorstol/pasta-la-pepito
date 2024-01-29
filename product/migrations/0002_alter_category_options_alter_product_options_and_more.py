# Generated by Django 4.1 on 2024-01-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Category"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ("rating",)},
        ),
        migrations.AddField(
            model_name="category",
            name="icon",
            field=models.ImageField(blank=True, upload_to="categories/"),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="image",
            field=models.ImageField(blank=True, upload_to="ingredients/"),
        ),
    ]
