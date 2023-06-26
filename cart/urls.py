from django.urls import path
from .views import CartView

urlpatterns = [
    path('cart/', CartView.as_view({'get': 'list'})),
    path('cart/add', CartView.as_view({'post': 'create'})),
    path('cart/delete/<int:product_id>/', CartView.as_view({'delete': 'destroy'})),
]


