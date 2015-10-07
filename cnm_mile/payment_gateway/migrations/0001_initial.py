# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulkUpload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('csv_file', models.FileField(upload_to=b'', verbose_name=b'CSV File')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name=b'Title')),
                ('author', models.CharField(max_length=40, verbose_name=b'Author')),
                ('cover_image', models.ImageField(upload_to=b'', verbose_name=b'Cover Image')),
                ('price', models.FloatField(max_length=5, verbose_name=b'Price')),
                ('availability', models.CharField(max_length=20, verbose_name=b'Availability')),
                ('description', models.TextField(max_length=240, verbose_name=b'Description')),
                ('inkling_product_id', models.CharField(max_length=40, verbose_name=b'Inkling Product ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=40, verbose_name=b'Last Name')),
                ('cnm_email', models.EmailField(max_length=40, verbose_name=b'CNM Email')),
                ('book_choice', models.CharField(max_length=40, verbose_name=b'Book Choice')),
            ],
        ),
    ]
