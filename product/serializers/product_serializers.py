from rest_framework import serializers

from product.models import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True) # no nosso modelo de products temos uma referencia de category, pois é o unico que queremos alterar

    class Meta:
        model = Product
        fileds = [
            'title',
            'description',
            'price',
            'active',
            'category'
        ]