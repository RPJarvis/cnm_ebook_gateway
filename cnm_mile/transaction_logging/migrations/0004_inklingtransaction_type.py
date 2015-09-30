# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_logging', '0003_auto_20150921_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='inklingtransaction',
            name='type',
            field=models.CharField(default='customer', max_length=12),
            preserve_default=False,
        ),
    ]
