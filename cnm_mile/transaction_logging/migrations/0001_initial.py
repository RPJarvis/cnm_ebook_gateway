# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InklingTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user_id', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=80)),
                ('success_or_fail', models.CharField(max_length=20)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TouchnetTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('user_id', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=80)),
                ('ammount', models.FloatField()),
                ('success_or_fail', models.CharField(max_length=20)),
                ('details', models.TextField()),
            ],
        ),
    ]
