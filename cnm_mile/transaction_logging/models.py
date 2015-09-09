from django.db import models

# Create your models here.
class TouchnetTransaction(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    user_id = models.EmailField()
    title = models.CharField(max_length=80)
    ammount = models.FloatField()
    success_or_fail = models.CharField(max_length=20)
    details = models.TextField()


class InklingTransaction(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    user_id = models.EmailField()
    title = models.CharField(max_length=80)
    success_or_fail = models.CharField(max_length=20)
    details = models.TextField()
