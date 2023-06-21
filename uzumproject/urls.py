from django.contrib import admin
from django.urls import path, include, re_path
from .yasg import urlpatterns as doc_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/', include('store.urls')),

]

urlpatterns += doc_url
