# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Tid',
            field=models.CharField(default=b'', editable=False, max_length=6),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
