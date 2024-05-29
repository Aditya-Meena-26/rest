from django.urls import path
from . import views

urlpatterns = [
    path('nearby-markets/', views.find_nearby_markets, name='find_nearby_markets'),
]
