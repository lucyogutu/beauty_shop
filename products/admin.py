"""
    register models for the admin site
"""
from django.contrib import admin

from .models import (
    Category,
    SubCategory,
    Attribute,
    Product,
    Variant,
    VariantAttribute,
    ProductSubCategory,
    ProductImage,
    ProductReview,
    Size,
    VariantSize,
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
        return ', '.join([subcat.name for subcat in obj.subcategories.all()])
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
    list_display = ('name', 'description', 'get_variants')
    list_display_links = ('name',)

    def get_variants(self, obj):
        """
            Display variants of a product
        """
        return ', '.join([c.name for c in obj.variants.all()])
    get_variants.short_description = 'Variants'


class ProductSubcategoryAdmin(admin.ModelAdmin):
    """
        Set up for product subcategories
        (connecter between a product and a subcategory)
    """
    list_display = ('product', 'subcategory')
    list_display_links = ('subcategory',)


class VariantAdmin(admin.ModelAdmin):
    """
        Set up for product
    """
    list_display = ('name', 'get_product')
    list_display_links = ('name',)

    def get_product(self, obj):
        """
            Display product
        """
        return obj.product
    get_product.short_description = 'Product'


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Attribute)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(VariantAttribute)
admin.site.register(ProductSubCategory, ProductSubcategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Size)
admin.site.register(VariantSize)
