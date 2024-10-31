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


class CategoryAdmin(admin.ModelAdmin):
    """
        Category Admin for modifying display of tables
    """
    list_display = ('name', 'get_subcategories')
    list_display_links = ('name',)

    def get_subcategories(self, obj):
        """
            Display subcategories of a category
        """
        return ', '.join([sc.name for sc in obj.subcategories.all()])
    get_subcategories.short_description = 'Subcategories'


class SubCategoryAdmin(admin.ModelAdmin):
    """
        Subcategory Admin
    """
    list_display = ('name', 'get_categories')
    list_display_links = ('name',)

    def get_categories(self, obj):
        """
            Display categories of a subcategory
        """
        return ', '.join([c.name for c in obj.category.all()])
    get_categories.short_description = 'Categories'


class ProductAdmin(admin.ModelAdmin):
    """
        Set up for product
    """
    list_display = ('name', 'description',  'price')
    list_display_links = ('name',)


class ProductSubcategoryAdmin(admin.ModelAdmin):
    """
        Set up for product subcategories
        (connecter between a product and a subcategory)
    """
    list_display = ('product', 'subcategory')
    list_display_links = ('subcategory',)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Attribute)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute)
admin.site.register(ProductSubCategory, ProductSubcategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
