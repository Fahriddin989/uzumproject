from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from .serializers import CartSerializer, CartDetailSerializer
from .models import Cart


class CartView(ModelViewSet):
    """ Вывод корзины пользователя
    """

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ Запрос корзины авторизованного пользователя
        """
        return Cart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """ Динамический вывод нужного сериализатора в зависимости от параметров
        """
        if self.action == 'list':
            return CartSerializer
        else:
            return CartDetailSerializer
