# views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

# View for processing orders
def process_order(request, pk):
    order = Order.objects.get(pk=pk)
    # Implement logic to process the order
    return redirect('order_detail', pk=pk)

# View for updating order status
def update_order_status(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status', '')
        order.status = new_status
        order.save()
        return redirect('order_detail', pk=pk)
    return render(request, 'update_order_status.html', {'order': order})

# View for tracking orders
class OrderTrackingView(DetailView):
    model = Order
    template_name = 'order_tracking.html'
    context_object_name = 'order'
