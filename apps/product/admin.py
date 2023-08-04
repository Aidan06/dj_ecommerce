from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price',
                    'in_stock', 'created_by']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
