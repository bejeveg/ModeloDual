# Generated by Django 3.0.5 on 2020-06-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0031_auto_20200615_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='correo',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='estado_actual',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
