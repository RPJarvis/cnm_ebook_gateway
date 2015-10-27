# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0005_remove_bulkupload_book_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulkupload',
            name='book_choice',
            field=models.CharField(default='whatever', max_length=40, verbose_name=b'Book Choice'),
            preserve_default=False,
        ),
    ]
