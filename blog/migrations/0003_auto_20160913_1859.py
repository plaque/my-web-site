# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 16:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 9, 13, 16, 59, 54, 804534, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
