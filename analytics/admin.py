from django.contrib import admin
from .models import Sales, Revenue, InventoryTurnover
# Register your models here.
admin.site.register(Sales)
admin.site.register(Revenue)
admin.site.register(InventoryTurnover)