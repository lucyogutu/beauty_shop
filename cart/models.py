"""
    This module contains all the models for a cart
"""
from django.contrib.auth.models import User
from django.db import models

from products.models import BaseModel, Product

# Create your models here.


class Cart(BaseModel):
    """
    Represents a shopping cart for the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Total price: {self.total_price}'


class CartItem(BaseModel):
    """
    Represents an item in the shopping cart
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product} x {self.quantity}'
