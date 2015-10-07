# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='site_id',
            field=models.CharField(default=1, max_length=2, verbose_name=b'UPay Site ID'),
        ),
    ]
