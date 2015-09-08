from django.db import models

# Create your models here.
class TouchnetTransaction(models.Model):
    date_created = models.DateTimeField(auto_now=True)




class InklingTransactin(models.Model):
    date_Created = models.DateTimeField(auto_now=True)