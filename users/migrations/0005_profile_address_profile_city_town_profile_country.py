# Generated by Django 4.2.7 on 2023-12-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='city_town',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]