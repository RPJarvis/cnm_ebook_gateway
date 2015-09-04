from django.db import models
from django.core.validators import validate_email


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=40)
    last_name = models.CharField(verbose_name="Last Name", max_length=40)
    cnm_email = models.EmailField(verbose_name="CNM Email", max_length=40)


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=40)
    author = models.CharField(verbose_name="Author", max_length=40)
    cover_image = models.ImageField(verbose_name="Cover Image")
    price = models.FloatField(verbose_name="Price", max_length=5)
    inkling_product_id = models.CharField(verbose_name="Inkling Product ID", max_length=15)
    #probably need isbns and junk here

#class PurchaseHistory(models.Model):



