# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='book_choice',
            field=models.CharField(default='dictionary', max_length=40),
            preserve_default=False,
        ),
    ]
