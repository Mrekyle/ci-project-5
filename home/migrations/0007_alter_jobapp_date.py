# Generated by Django 4.2.9 on 2024-02-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_jobapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapp',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]