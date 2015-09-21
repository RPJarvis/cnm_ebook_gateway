# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_logging', '0002_auto_20150910_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='inklingtransaction',
            name='first_name',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inklingtransaction',
            name='last_name',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touchnettransaction',
            name='first_name',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touchnettransaction',
            name='last_name',
            field=models.CharField(default='test', max_length=40),
            preserve_default=False,
        ),
    ]
