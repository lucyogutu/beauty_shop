# Generated by Django 5.1.2 on 2024-11-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price_alter_size_size_productimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
