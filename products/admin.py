from .models import Category, Product
from django.contrib import admin


# Register your models here.
@admin.register(Category)
class CustomCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Product)
class CustomProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "category",
        "title",
        "description",
        "price",
        "slug",
        "published",
        "author",
        "status",
    ]

    prepopulated_fields = {'slug': ('title',), }
