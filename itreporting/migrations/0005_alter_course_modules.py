# Generated by Django 4.2.7 on 2023-12-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0004_remove_course_modules_course_modules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(to='itreporting.module'),
        ),
    ]
