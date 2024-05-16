from django.db import models

class Category(models.Model): # Importando a classe Model de models do Django que defini o modelo do banco de dados
    title = models.CharField(max_length=100) # Criando um campo de caracteres para o título
    slug = models.SlugField(unique=True) # Criando um campo slug para uma identificação única
    description = models.TextField(max_length=500, blank=True, null=True) # Criando um campo de texto para a descrição e habilitando o campo para receber valores vazios e nulos
    active = models.BooleanField(default=True) # Criando um campo boleano e habilitando o mesmo como padrão, que informa que ele esta ativo

    def __unicode__(self):  # Método que retorna a representação de string do objeto, que neste caso seria o titulo
        return self.title