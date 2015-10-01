# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0006_bulkupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulkupload',
            name='emails',
        ),
        migrations.RemoveField(
            model_name='bulkupload',
            name='first_names',
        ),
        migrations.RemoveField(
            model_name='bulkupload',
            name='last_names',
        ),
        migrations.AddField(
            model_name='bulkupload',
            name='csv_file',
            field=models.FileField(default='upload_a_file.txt', upload_to=b'', verbose_name=b'CSV File'),
            preserve_default=False,
        ),
    ]
