# Generated by Django 3.0.8 on 2020-08-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200809_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug_padrao'),
            preserve_default=False,
        ),
    ]