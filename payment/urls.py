# urls.py

from django.urls import path
from .views import checkout

urlpatterns = [
    path('checkout/<int:product_price>/', checkout, name='checkout'),
]
