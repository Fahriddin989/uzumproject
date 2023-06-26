from django.urls import path
from .views import OrderView

urlpatterns = [
    path('orders/all', OrderView.as_view({'get': 'list'})),
    path('orders/<int:pk>', OrderView.as_view({'get': 'retrieve'})),
    path('orders/create', OrderView.as_view({'post': 'create'})),
    path('orders/delete/<int:pk>', OrderView.as_view({'delete': 'destroy'}))
]