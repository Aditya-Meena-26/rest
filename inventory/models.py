from django.db import models
from django.utils import timezone
from product.models import Product

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    stock_level = models.CharField(max_length=20)
    expiration_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"
