"""
    This module contains all the models for an Order
"""

from django.contrib.auth.models import User
from django.db import models

from products.models import BaseModel, Product

# Create your models here.


class Order(BaseModel):
    """
    Represents an order made by the user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            f"Order {self.id} for {self.user}. "
            f"Total price: {self.total_price}"
        )


class OrderItem(BaseModel):
    """
    Represents an order item
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return (
            f'{self.product} x {self.quantity} '
            f'for Order {self.order}'
        )
