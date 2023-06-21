from rest_framework import viewsets, generics
from .models import Product, Category, Executor
from rest_framework import permissions
from .serializers import (ProductSerializer, CategorySerializer,
                          ExecutorSerializer, CreateExecutorSerializer)
from .permissions import IsAuthorOrIsAdmin, IsCreaterOrIsAdmin


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthorOrIsAdmin]


class ExecutorView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class CreateExecutorView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DetailExecutorView(generics.RetrieveUpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_classes = [IsCreaterOrIsAdmin]


