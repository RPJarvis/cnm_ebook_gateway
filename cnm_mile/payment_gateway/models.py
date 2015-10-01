from django.db import models
from transaction_logging.models import InklingTransaction

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
    price = models.FloatField(verbose_name="Price", max_length=5)
    availability = models.CharField(verbose_name="Availability", max_length=20)
    description = models.TextField(verbose_name="Description", max_length=240)
    inkling_product_id = models.CharField(verbose_name="Inkling Product ID", max_length=40)

    def __unicode__(self):
        return self.title


class BulkUpload(models.Model):
    csv_file = models.FileField(verbose_name='CSV File')

    def __unicode__(self):
        return self.csv_file



