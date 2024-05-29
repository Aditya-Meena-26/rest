from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from product.models import Product 

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()

    def __str__(self):
        return f"Review for {self.product} by {self.buyer}"
