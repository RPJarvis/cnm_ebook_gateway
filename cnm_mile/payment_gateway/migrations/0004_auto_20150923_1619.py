# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0003_userinfo_book_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(default='CNM', max_length=20, verbose_name=b'Availability'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='book_choice',
            field=models.CharField(max_length=40, verbose_name=b'Book Choice'),
        ),
    ]
