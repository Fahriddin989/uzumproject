from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone

# from users.models import CustomUser

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    icon = models.ImageField('Иконка категории', upload_to='images/category/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ExtraImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='extra_images/')

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=100, blank=True)
    description = RichTextField()
    quantity_in_stock = models.IntegerField('Количество на складе', default=1)
    image = models.ImageField(upload_to='main_image/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(decimal_places=2, max_digits=3,
                                   blank=True, null=True, validators=[MaxValueValidator(100)])
    # new = models.BooleanField(default=True)
    executor = models.ForeignKey('Executor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    process = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.pk:  # Применяем эту проверку только для новых объектов, а не при обновлении
            user = kwargs.get('user')  # Получаем пользователя из аргументов
            if user and not user.is_superuser:
                self.process = True  # Для неадминистраторов устанавливаем process в True

        super().save(*args, **kwargs)

    # def get_price(self):
    #     return (self.price - self.price * (self.discount_price / 100))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(default=0,
                                      validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Рейтинг и отзыв'
        verbose_name_plural = 'Рейтинги и отзывы'
        unique_together = ('user', 'product')


class Executor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='seller/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


