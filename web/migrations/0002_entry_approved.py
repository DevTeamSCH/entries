# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-11 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]