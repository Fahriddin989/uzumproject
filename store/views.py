from rest_framework import viewsets, generics
from .models import Product, Category, Executor, Rating
from rest_framework import permissions
from .serializers import (ProductSerializer, CategorySerializer,
                          ExecutorSerializer, CreateExecutorSerializer, CreateRatingSerializer)
from .permissions import IsAuthorOrIsAdmin, IsCreatorOrIsAdmin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from .pagination import ProductPagination

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price']
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'short_description', 'description']
    pagination_class = ProductPagination

    def get_queryset(self):
        products = Product.objects.all().annotate(rating=Avg('ratings__rating'))
        return products

    def post(self, request, *args, **kwargs):
        users_executor = request.user.executor_set.all()
        executor = Executor.objects.get(id=request.POST['executor'])
        if executor is not None and executor in users_executor:
            return self.create(request, *args, **kwargs)
        return Response(data='Вы указали неправильный идентификатор исполнителя', status=status.HTTP_400_BAD_REQUEST)


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
    permission_classes = [IsCreatorOrIsAdmin]


class RatingView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class UpdateRating(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer
    permission_classes = [IsCreatorOrIsAdmin]

