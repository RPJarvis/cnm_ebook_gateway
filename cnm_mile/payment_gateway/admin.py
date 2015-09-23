from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'price', 'availability', 'inkling_product_id', 'cover_image', 'description']

admin.site.register(Product, ProductAdmin)
