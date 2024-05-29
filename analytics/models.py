# models.py
from django.db import models
from product.models import Product
class Sales(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class Revenue(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class InventoryTurnover(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    turnover_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
