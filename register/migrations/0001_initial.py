# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=500)),
                ('user_email', models.CharField(max_length=500)),
                ('user_mobile', models.IntegerField()),
                ('user_password', models.CharField(max_length=500)),
                ('user_dob', models.DateField(verbose_name='date')),
                ('user_credits', models.IntegerField(default=1000)),
            ],
        ),
    ]
