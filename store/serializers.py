from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    def get_discounted_price(self, obj):
        discount_price = obj.price * (1 - obj.discount)
        return discount_price

    class Meta:
        model = Product
        fields = ('id', 'category', 'name', 'short_description', 'description',
                  'quantity_in_stock', 'image', 'price', 'discount', 'new', 'discount_price')
