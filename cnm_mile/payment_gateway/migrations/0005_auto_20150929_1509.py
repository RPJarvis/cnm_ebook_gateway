# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0004_auto_20150923_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inkling_product_id',
            field=models.CharField(max_length=40, verbose_name=b'Inkling Product ID'),
        ),
    ]
