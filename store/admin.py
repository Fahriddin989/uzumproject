from django.contrib import admin
from .models import Product, Category, ExtraImage, Executor, Rating


class ImagesAdmin(admin.TabularInline):
    model = ExtraImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]


admin.site.register(Category)
admin.site.register(Executor)
admin.site.register(Rating)
