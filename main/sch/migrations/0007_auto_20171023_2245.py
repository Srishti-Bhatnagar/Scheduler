# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-23 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0006_auto_20171023_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyval',
            name='key',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='keyval',
            name='value',
            field=models.CharField(db_index=True, default=b'', max_length=4),
        ),
    ]
