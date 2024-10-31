"""
    This module represents all module for the product app

    One Category has many SubCategories
    One subcategory has one category

    One SubCategory has many Product
    One Product has many SubCategories

    One Product has many ProductImages
    One ProductImage has one Product

    One Product has many Product Reviews
    One ProductReview has one Product

    One Product has many Attributes
    One Attribute can exist in many Products ... many to many
"""

import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


SIZE_TYPE_CHOICES = {
    "ml": "ml",
    "l": "l",
    "g": "g",
    "kg": "kg",
    "S": "small",
    "M": "medium",
    "L": "large",
}


class BaseModel(models.Model):
    """
    Base model for all other models.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True, max_length=100, unique=True)

    class Meta:
        """
            Abstracts the base class for all models
        """
        abstract = True


class Category(BaseModel):
    """
        Represents a category
    """
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class SubCategory(BaseModel):
    """
        Represents a subcategory under a category
    """
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='subcategories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Attribute(BaseModel):
    """
        Represents an attribute of a product
    """
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    """
        Represents a product
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    subcategory = models.ManyToManyField(
        SubCategory,
        through='ProductSubCategory')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    # def get_first_variant_price(self):
    #     """
    #         Get the price of the first variant and display
    #     """
    #     first_variant = self.variants.first()
    #     return first_variant.price if first_variant else None


class ProductSubCategory(BaseModel):
    """
        This is a connection between a product and a subcategory
    since it has many to many relationship
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} : {self.subcategory}'


class Variant(models.Model):
    """
        Represents a variant of a product
        e.g Product Nivea has Nivea Cocoa and Nivea Shea Butter
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.product} {self.name}'


class Size(models.Model):
    """
        Represents a size of a product
        e.g 400g, 450ml etc or Small
    """
    size = models.IntegerField(
        null=True,
        blank=True,
    )
    size_type = models.CharField(
        max_length=2,
        choices=SIZE_TYPE_CHOICES,
        null=True,
        blank=True,
    )

    def __str___(self):
        return f'{self.size}'


class VariantSize(models.Model):
    """
        Represents a size of a product variant
        e.g Product Nivea Cocoa has 400g and 450g sizes
    """
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.variant} : {self.size} - {self.price}'


class VariantAttribute(BaseModel):
    """
        This is a connection between a product and an attribute
        since it has many to many relationship
    """
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.variant} : {self.attribute} - {self.value}'


class ProductImage(BaseModel):
    """
        Represents an image of a product
    """
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Variant, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.id)
        super().save(*args, **kwargs)


class ProductReview(BaseModel):
    """
        Represents a review of a product
    """
    rating = models.PositiveIntegerField()
    review = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'review-{self.product.name}')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.rating}, {self.review}'
