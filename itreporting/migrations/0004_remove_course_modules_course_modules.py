# Generated by Django 4.2.7 on 2023-12-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0003_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='modules',
        ),
        migrations.AddField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(null=True, to='itreporting.module'),
        ),
    ]
