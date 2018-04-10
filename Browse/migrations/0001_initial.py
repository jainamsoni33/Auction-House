# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-21 14:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bought',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=2500)),
                ('item_desc', models.TextField(max_length=2500)),
                ('sell_price', models.IntegerField(default=0, null=True)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expired',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=2500)),
                ('item_desc', models.TextField(max_length=2500)),
                ('created_on', models.DateTimeField(default=datetime.datetime(2017, 9, 21, 14, 36, 54, 684731, tzinfo=utc))),
                ('min_price', models.IntegerField(null=True)),
                ('buy_now_price', models.IntegerField(null=True)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=2500)),
                ('item_desc', models.TextField(max_length=2500)),
                ('cur_highest_bid', models.IntegerField(default=0, null=True)),
                ('min_price', models.IntegerField(null=True)),
                ('buy_now_price', models.IntegerField(null=True)),
                ('cur_highest_bidder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='highest_bidder', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
