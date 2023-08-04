from rest_framework.serializers import ModelSerializer

from apps.product.apps import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'photo', 'in_stock')
