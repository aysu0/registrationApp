# Generated by Django 4.2.7 on 2023-12-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0006_coursegroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(related_name='courses', to='itreporting.module'),
        ),
    ]
