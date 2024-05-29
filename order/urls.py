
from django.urls import path
from .views import OrderListView, OrderDetailView, process_order, update_order_status, OrderTrackingView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/process/', process_order, name='process_order'),
    path('orders/<int:pk>/update-status/', update_order_status, name='update_order_status'),
    path('orders/<int:pk>/track/', OrderTrackingView.as_view(), name='order_tracking'),
]
