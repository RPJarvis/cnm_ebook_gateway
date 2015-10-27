# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0004_bulkupload_book_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulkupload',
            name='book_choice',
        ),
    ]
