# Generated by Django 3.2 on 2023-12-24 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newitem',
            options={'verbose_name_plural': 'New Item'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
    ]
