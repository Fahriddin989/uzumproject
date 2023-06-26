from _decimal import Decimal

from django.db import models
from django.conf import settings
from store.models import Product


class Order(models.Model):
    """ Модель информации о заказе
    """

    STATUS = (
        ('SUCCESS', 'Успех'),
        ('TIMEOUT', 'Закрытие по таймауту'),
        ('CREATED_PAY', 'Создание транзакции'),
        ('FINISHED', 'Окончание транзакции'),
        ('PAID', 'Оплачивается'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField('Номер заказа', max_length=17, unique=True)
    order_status = models.CharField('Статус заказа', choices=STATUS, default='PAID', max_length=11)
    order_comment = models.CharField('Комментарий к заказу', max_length=1000, blank=True)
    order_time = models.DateTimeField('Время заказа', auto_now_add=True)

    signer_firstname = models.CharField('Имя заказчика', max_length=50)
    signer_lastname = models.CharField('Фамилия заказчика', max_length=50)
    signer_address = models.CharField('Адрес доставки', max_length=1000)
    signer_phone = models.CharField('Контактный телефон', max_length=11)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_time']

    def __str__(self):
        return f'Заказ {self.order_number}'

    def to_pay(self):
        """ Подсчет общей стоимости товаров в корзине
        """
        return sum(item.total_price() for item in self.order_items.all())


class OrderItem(models.Model):
    """ Модель товара в заказе
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, related_name='product_items', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def __str__(self):
        return f'{self.product.id} - {self.product.name}'

    def total_price(self) -> Decimal:
        return self.amount * self.product.price
