from rest_framework import routers
from .views import *
from django.urls import path

#
# router = routers.DefaultRouter()
# router.register('products', ProductListView)

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),

    path('executors/', ExecutorView.as_view(), name='executor'),
    path('executors/<int:pk>', DetailExecutorView.as_view(), name='executor-detail'),
    path('executors/new', CreateExecutorView.as_view(), name='executor-create'),

]
