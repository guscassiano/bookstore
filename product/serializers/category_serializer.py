from rest_framework import serializers

from product.models.category import Category

class CategorySerializer(serializers.ModelSerializer): # neste caso não adicionamos nada pq não queremos nenhuma alteração, somente que retorne todos os campos do modelo de category
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active'
        ]

        extra_kwargs = {"slug": {"required": False}}