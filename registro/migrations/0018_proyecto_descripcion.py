# Generated by Django 3.0.5 on 2020-06-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0017_auto_20200608_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
