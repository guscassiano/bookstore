import factory  # Factory é uma biblioteca para construir dados falsos e mocks

from product.models import Product, Category

class CategoryFactory(factory.django.DjangoModelFactory): # facory é um espelho dos nossos modelos, esta classe cria os modelos falsos em Django
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    descrption = factory.Faker('pystr')
    active = factory.Iterator([True, False]) # este campo irá trocar entre true e false devido ao iterador

    class Meta:
        model: Category  # informamos sempre o modelo que iremos utilizar, neste caso será o Category para criar essa fabrica

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.Faker('pyint')
    category = factory.LazyAttribute(CategoryFactory) # o lazy Attrbute indica que a atribuição será feita apenas quando o atributo CategoryFactory for acessado
    title = factory.Faker('pystr')

    @factory.post_generation # Define um método de geração pós-fábrica. Este método será executado após a criação da instância do modelo.
    def category(self, create, extracted, **kwargs): # create é um sinalizador booleano que indica se a instância está sendo criada ou construída. extracted contém os valores passados durante a criação.
        if not create: #  Se o modelo não estiver sendo criado (por exemplo, se estiver sendo apenas construído), o método para aqui.
            return

        if extracted: # Se valores foram passados durante a criação, este bloco é acionado.
            for category in extracted:
                self.category.add(category)  # Adiciona as categorias extraídas à instância do ProducyFactory.

    class Meta:
        model: Product