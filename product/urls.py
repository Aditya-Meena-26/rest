from django.urls import path
from .views import ProductListView, ProductDetailView, create_product, edit_product, delete_product

app_name = 'products'

urlpatterns = [
    # Product listings
    path('', ProductListView.as_view(), name='product_list'),

    # Product detail
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Product creation
    path('create/', create_product, name='create_product'),

    # Product editing
    path('<int:pk>/edit/', edit_product, name='edit_product'),

    # Product deletion
    path('<int:pk>/delete/', delete_product, name='delete_product'),
]
