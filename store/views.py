from rest_framework import viewsets
from .models import Product
from rest_framework import permissions
from .serializers import ProductSerializer


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]







