from django.db import models
from django.core.validators import validate_email


class UserInfo(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=40)
    last_name = models.CharField(verbose_name="Last Name", max_length=40)
    cnm_email = models.EmailField(verbose_name="CNM EMail", max_length=40)


