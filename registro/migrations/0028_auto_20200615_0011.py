# Generated by Django 3.0.5 on 2020-06-15 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0027_auto_20200614_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner_items',
            old_name='orden_aparcion',
            new_name='orden_aparicion',
        ),
    ]