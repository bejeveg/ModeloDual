# Generated by Django 3.0.5 on 2020-06-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0018_proyecto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
