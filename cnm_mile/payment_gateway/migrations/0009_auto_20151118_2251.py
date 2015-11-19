# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mobile_cover_image',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'Mobile Cover Image'),
        ),
        migrations.AlterField(
            model_name='bulkupload',
            name='book_choice',
            field=models.CharField(max_length=40, verbose_name=b'Book Choice', choices=[('New Mexico History', 'New Mexico History')]),
        ),
    ]
