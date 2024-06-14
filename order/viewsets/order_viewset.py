from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]  # Basic defini qual será o tipo de autenticação
    permission_classes = [
        IsAuthenticated
    ]  # Ele intercepta dentro do middleware se o usuário q fez a requisição da API Rest esta autenticado ou não

    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("id")
