# Generated by Django 5.1.2 on 2024-10-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]