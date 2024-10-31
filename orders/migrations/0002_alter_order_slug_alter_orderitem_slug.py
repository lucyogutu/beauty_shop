# Generated by Django 5.1.2 on 2024-10-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
