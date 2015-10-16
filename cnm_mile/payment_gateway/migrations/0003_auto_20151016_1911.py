# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0002_product_site_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulkupload',
            name='csv_file',
        ),
        migrations.AddField(
            model_name='bulkupload',
            name='csv_field',
            field=models.TextField(default=',', verbose_name=b'CSV Field'),
            preserve_default=False,
        ),
    ]
