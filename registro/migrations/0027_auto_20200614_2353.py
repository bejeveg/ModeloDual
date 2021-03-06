# Generated by Django 3.0.5 on 2020-06-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0026_remove_banner_items_alternative_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_items',
            name='image',
            field=models.ImageField(default=1, upload_to='banner_gallery/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner_items',
            name='redirect_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
