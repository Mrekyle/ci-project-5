# Generated by Django 4.2.9 on 2024-01-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_jobcategory_alter_jobpost_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]