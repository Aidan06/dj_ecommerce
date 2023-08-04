from django.urls import path

from apps.product.apps import Product

urlpatterns = [
    path('', Product)
]