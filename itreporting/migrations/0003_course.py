# Generated by Django 4.2.7 on 2023-12-05 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itreporting', '0002_alter_module_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('modules', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='itreporting.module')),
            ],
        ),
    ]
