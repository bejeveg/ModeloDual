# Generated by Django 3.0.5 on 2020-06-10 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0020_auto_20200609_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('alternative_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]