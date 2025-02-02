from django.db import models
from transaction_logging.models import InklingTransaction
from django import forms


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=40)
    last_name = models.CharField(verbose_name="Last Name", max_length=40)
    cnm_email = models.EmailField(verbose_name="CNM Email", max_length=40)
    book_choice = models.CharField(verbose_name="Book Choice", max_length=40)

    def __unicode__(self):
        return self.cnm_email


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=40)
    author = models.CharField(verbose_name="Author", max_length=40)
    cover_image = models.ImageField(verbose_name="Cover Image")
    mobile_cover_image = models.ImageField(verbose_name="Mobile Cover Image", default='')
    price = models.FloatField(verbose_name="Price", max_length=5)
    availability = models.CharField(verbose_name="Availability", max_length=20)
    description = models.TextField(verbose_name="Description", max_length=240)
    site_id = models.CharField(verbose_name="UPay Site ID", max_length=2, default=1)
    inkling_product_id = models.CharField(verbose_name="Inkling Product ID", max_length=40)


    def __unicode__(self):
        return self.title

#This broke migrate twice, should probably be elsewhere

bulk_choices = list()
products = Product.objects.all()
for product in products:
    bulk_choices.append((product.title, product.title))


class BulkUpload(models.Model):
    csv_field = models.TextField(verbose_name="CSV Field")
    #book_choice = forms.ModelMultipleChoiceField(required=True, queryset=Product.objects.all())
    book_choice = models.CharField(verbose_name="Book Choice", max_length=40, choices=bulk_choices)
    #book_choice = models.CharField(verbose_name="Book Choice", max_length=40, choices='')

    def __unicode__(self):
        return 'CSV Field'
