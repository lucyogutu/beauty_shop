# Generated by Django 5.1.2 on 2024-10-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_attribute_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ManyToManyField(related_name='subcategories', to='products.category'),
        ),
    ]