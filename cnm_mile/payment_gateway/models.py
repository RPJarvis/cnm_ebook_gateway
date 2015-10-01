from django.db import models
from payment_gateway import inkling_tools
from transaction_logging.models import InklingTransaction
from django.core.validators import validate_email


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=40)
    last_name = models.CharField(verbose_name="Last Name", max_length=40)
    cnm_email = models.EmailField(verbose_name="CNM Email", max_length=40)
    book_choice = models.CharField(verbose_name="Book Choice", max_length=40)

    def __str__(self):
        return self.cnm_email


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=40)
    author = models.CharField(verbose_name="Author", max_length=40)
    cover_image = models.ImageField(verbose_name="Cover Image")
    price = models.FloatField(verbose_name="Price", max_length=5)
    availability = models.CharField(verbose_name="Availability", max_length=20)
    description = models.TextField(verbose_name="Description", max_length=240)
    inkling_product_id = models.CharField(verbose_name="Inkling Product ID", max_length=40)

    def __str__(self):
        return self.title
    #probably need isbns and junk here

class BulkUpload(models.Model):
    first_names = models.TextField(verbose_name="First Names")
    last_names = models.TextField(verbose_name="Last Names")
    emails = models.TextField(verbose_name="Emails")

 #   def inkling_bulk(self):




