from rest_framework import serializers

from order.models import Order
from product.models import Product
from product.serializers.product_serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):  # O ModelSerializer extende o modelos e tambem possui diversas funções, uma de suas maiores qualidades é podermos reescrever suas funções
    product = ProductSerializer(required=True, many=True) # o many=True é habilitado pois podemos ter mais de um produto para uma determinada ordem, um Order pode ter múltiplos Product
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True) #em qureyset informamos que todos os objetos Product são válidos para esta relação, será usado só pra escrita e permite múltiplos produtos
    total = serializers.SerializerMethodField() # este é um exemplo de extensão, este campo não foi adicionado no models do order, porém esta sendo add aqui graças ao serializers, e o SerializerMethodField() que cria este campo

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()]) # somando todos os produtos de uma determinada ordem
        return total

    class Meta: # Aqui dizemos quais campos serão exibidos no JSON, normlamente sigmos os campos criados na classe principal
        model = Order #modelo que o serializer irá representar
        fields = ['product', 'total', 'user', 'products_id'] #estes campos serão incluidos no JSON
        extra_kwargs = {'product': {'required':False}} #fornece opcionalmente argumentos adicionas para o campo product

    def create(self, validated_data): #create é sobrescrito para personalizar a criação de uma instância de Order.
        product_data = validated_data.pop('products_id') #extrai os IDs dos produtos validated_data
        user_data = validated_data.pop('user') #extrai os dados do usuário.

        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product) #adiciona cada produto ao order

        return order