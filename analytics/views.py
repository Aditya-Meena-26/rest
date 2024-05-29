# views.py
from django.shortcuts import render
from .models import Sales, Revenue, InventoryTurnover

def sales_report(request):
    sales_data = Sales.objects.all()
    return render(request, 'sales_report.html', {'sales_data': sales_data})
