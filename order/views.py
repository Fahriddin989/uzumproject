from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderListSerializer


class OrderView(ModelViewSet):
    """ Вывод информации о заказе
    """

    parser_classes = (parsers.MultiPartParser,)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ Запрос ордеров авторизованного пользователя
        """
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        """ Динамический вывод нужного сериализатора в зависимости от параметров
        """
        if self.action == 'list':
            return OrderListSerializer
        else:
            return OrderSerializer

    def perform_create(self, serializer):
        """ Перенос информации из корзины в ордер: удаление корзины, создание ордера
        """
        order = serializer.save()
        carts = Cart.objects.filter(user=self.request.user.id)
        for cart in carts:
            order_products = OrderItem()
            order_products.product = cart.product
            order_products.amount = cart.amount
            order_products.order = order
            order_products.save()
            cart.delete()
        return order
