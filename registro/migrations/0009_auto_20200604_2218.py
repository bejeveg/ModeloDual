# Generated by Django 3.0.5 on 2020-06-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0008_auto_20200604_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asesoresinterno',
            name='departamento',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
