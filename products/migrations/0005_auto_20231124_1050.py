# Generated by Django 3.2 on 2023-11-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.DeleteModel(
            name='ProductRating',
        ),
    ]
