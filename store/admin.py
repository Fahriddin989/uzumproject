from django.contrib import admin
from .models import Product, Category, ExtraImage, Executor, Rating


class ImagesInline(admin.TabularInline):
    model = ExtraImage
    extra = 1


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, RatingInline]
    list_display = ('id', 'name')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'rating')


admin.site.register(Category)
admin.site.register(Executor)
