# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0006_auto_20170921_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expired',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 23, 8, 31, 49, 865905, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
