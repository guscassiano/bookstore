from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):  # O ModelSerializer extende o modelos e tambem possui diversas funções, uma de suas maiores qualidades é podermos reescrever suas funções
    product = ProductSerializer(required=True, many=True) # o many=True é habilitado pois podemos ter mais de um produto para uma determinada ordem
    total = serializers.SerializerMethodField() # este é um exemplo de extensão, este campo não foi adicionado no models do order, porém esta sendo add aqui graças ao serializers, e o erializerMethodField() que cria este campo

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()]) # somando todos os produtos de uma determinada ordem
        return total

    class Meta: # Aqui dizemos quais campos serão exibidos no JSON, normlamente sigmos os campos criados na classe principal
        model: Product
        fields = ['product', 'total']