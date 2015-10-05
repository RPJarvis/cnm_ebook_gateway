from django.contrib import admin
from .models import Product, BulkUpload
from transaction_logging.models import InklingTransaction
import inkling_tools


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'price', 'availability', 'inkling_product_id', 'cover_image', 'description']

admin.site.register(Product, ProductAdmin)


class BulkUploadAdmin(admin.ModelAdmin):
    fields = ['csv_file']

admin.site.register(BulkUpload, BulkUploadAdmin)
