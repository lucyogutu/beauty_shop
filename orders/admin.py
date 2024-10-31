"""
    register order models on the admin site
"""
from django.contrib import admin

from .models import (
    Order,
    OrderItem,
)

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
