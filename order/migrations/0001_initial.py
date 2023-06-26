# Generated by Django 4.2.2 on 2023-06-26 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=17, unique=True, verbose_name='Номер заказа')),
                ('order_status', models.CharField(choices=[('SUCCESS', 'Успех'), ('TIMEOUT', 'Закрытие по таймауту'), ('CREATED_PAY', 'Создание транзакции'), ('FINISHED', 'Окончание транзакции'), ('PAID', 'Оплачивается')], default='PAID', max_length=11, verbose_name='Статус заказа')),
                ('order_comment', models.CharField(blank=True, max_length=1000, verbose_name='Комментарий к заказу')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='Время заказа')),
                ('signer_firstname', models.CharField(max_length=50, verbose_name='Имя заказчика')),
                ('signer_lastname', models.CharField(max_length=50, verbose_name='Фамилия заказчика')),
                ('signer_address', models.CharField(max_length=1000, verbose_name='Адрес доставки')),
                ('signer_phone', models.CharField(max_length=11, verbose_name='Контактный телефон')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-order_time'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='order.order')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказа',
            },
        ),
    ]