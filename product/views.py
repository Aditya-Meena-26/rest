from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

@login_required
def create_product(request):
    if request.method == 'POST':
        
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
       
        form = ProductForm()
        return render(request, 'product_create.html', {'form': form})
        pass

@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        
        form = ProductForm(instance=product)
        return render(request, 'product_edit.html', {'form': form})
       

@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')
