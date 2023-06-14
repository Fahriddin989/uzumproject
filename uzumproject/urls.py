from django.contrib import admin
from django.urls import path, include ,re_path
from rest_framework import routers
from store.views import ProductView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

router = routers.DefaultRouter()
router.register(r'api/product', ProductView)


urlpatterns += router.urls