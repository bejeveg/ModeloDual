# Generated by Django 3.0.5 on 2020-06-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0024_banner_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner_items',
            name='redirect_page_section',
            field=models.CharField(blank=True, choices=[('Proyectos', 'Proyectos'), ('Album', 'Album'), ('Empresas', 'Empresas')], max_length=30, null=True),
        ),
    ]