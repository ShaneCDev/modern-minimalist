# Generated by Django 4.2.1 on 2023-06-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=256, null=True, unique=True),
        ),
    ]