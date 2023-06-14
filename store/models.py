from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

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
    description =  models.TextField()
    image = models.ImageField(upload_to='main_image/')
    # price = models.DecimalField(max_digits=10, decimal_places=2)








