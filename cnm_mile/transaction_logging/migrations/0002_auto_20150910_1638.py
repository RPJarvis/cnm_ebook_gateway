# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_logging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touchnettransaction',
            old_name='ammount',
            new_name='amount',
        ),
    ]
