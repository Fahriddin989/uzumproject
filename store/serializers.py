from rest_framework import serializers
from .models import Product, Category, Executor
from users.serializers import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    def get_discounted_price(self, instance):
        if instance.discount is not None:
            return instance.price - instance.price * (instance.discount / 100)
        else:
            return instance.price

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'short_description', 'description',
                  'quantity_in_stock', 'image', 'price', 'discount', 'new', 'discounted_price')


class ExecutorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'


class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'
