# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0005_auto_20150929_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_names', models.TextField(verbose_name=b'First Names')),
                ('last_names', models.TextField(verbose_name=b'Last Names')),
                ('emails', models.TextField(verbose_name=b'Emails')),
            ],
        ),
    ]
