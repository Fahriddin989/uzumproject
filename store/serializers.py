from rest_framework import serializers
from .models import Product, Category, Executor, Rating
from users.serializers import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()
    rating = serializers.FloatField()

    def get_discounted_price(self, instance):
        if instance.discount is not None:
            return instance.price - instance.price * (instance.discount / 100)
        else:
            return instance.price

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'short_description', 'description', 'executor',
                  'quantity_in_stock', 'image', 'price', 'discount', 'created_at', 'discounted_price', 'rating')


class ExecutorSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'


class CreateExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class CreateRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('user', 'product', 'rating', 'comment')

    # def create(self, validated_data):
    #
