from django.db import models
from django.contrib.auth.models import User
from product.models.product import Product

class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    #product: Este é um campo de muitos-para-muitos (ManyToManyField) que se relaciona com o modelo Product definido em product.models.product. Isso permite que um pedido contenha vários produtos e que um produto possa estar em vários pedidos. O argumento blank=False indica que este campo não pode ser deixado em branco.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user: Este é um campo de chave estrangeira (ForeignKey) que se relaciona com o modelo User, representando o usuário que fez o pedido. O argumento CASCATE indica que ao deletar o usuário será também removido todos os dados deste no banco de dados.