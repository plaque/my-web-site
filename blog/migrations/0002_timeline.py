# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
        ),
    ]
