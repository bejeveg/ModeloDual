# Generated by Django 3.0.5 on 2020-06-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0019_auto_20200609_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='url_folder',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='domicilio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='estado_actual',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='red_social_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asesoresexterno',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='asesoresexterno',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='asesoresinterno',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='asesoresinterno',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='den_social',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='giro',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='url_logo',
            field=models.URLField(),
        ),
    ]
