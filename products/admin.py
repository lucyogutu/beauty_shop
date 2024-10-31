"""
    register models for the admin site
"""
from django.contrib import admin

from .models import (
    Category,
    SubCategory,
    Attribute,
    Product,
    ProductAttribute,
    ProductSubCategory,
    ProductImage,
    ProductReview
)

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(ProductSubCategory)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
