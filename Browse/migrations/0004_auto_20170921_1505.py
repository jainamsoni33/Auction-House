# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 15:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Browse', '0003_auto_20170921_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_logo',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='expired',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 21, 15, 5, 9, 439545, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='items',
            name='created_on',
            field=models.DateTimeField(null=True),
        ),
    ]