# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170717_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='Location',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='Photographer',
            field=models.CharField(db_index=True, max_length=1000, null=True),
        ),
    ]
