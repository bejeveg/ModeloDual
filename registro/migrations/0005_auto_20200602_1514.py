# Generated by Django 3.0.5 on 2020-06-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20200601_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='red_social',
            field=models.CharField(blank=True, choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter')], max_length=30),
        ),
    ]
