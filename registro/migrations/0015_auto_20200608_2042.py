# Generated by Django 3.0.5 on 2020-06-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0014_proyecto_fecha_de_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud_alumno',
            name='s_semestre',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud_alumno',
            name='s_correo',
            field=models.EmailField(max_length=254),
        ),
    ]