from django.db import models
from product.models.category import Category

class Product(models.Model):
    title = models.CharField(max_length=100) # Criando um campo de caracteres para o título
    description = models.TextField(max_length=500, blank=True, null=True) # Criando um campo de texto para a descrição e habilitando o campo para receber valores vazios e nulos
    price = models.PositiveIntegerField(null=True) # Criando campo de números inteiros e positivos e habilitado o campo nulo
    active = models.BooleanField(default=True) # Criando um campo boleano e habilitando o mesmo por padrão ativo
    category = models.ManyToManyField(Category, blank=True) # Criando um relacionamento da classe Category de muitos para muitos e habilitando os valores nulos, assim permite que cadastre o produto para de uma categoria

    def __str__(self):
        return self.title