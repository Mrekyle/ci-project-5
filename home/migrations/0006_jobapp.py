# Generated by Django 4.2.9 on 2024-01-30 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_jobpost_date_created_alter_jobpost_job_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('resume', models.ImageField(blank=True, null=True, upload_to='')),
                ('cover_letter', models.CharField(blank=True, max_length=500, null=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.jobpost')),
            ],
            options={
                'verbose_name_plural': 'Job Application',
            },
        ),
    ]
