# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-10 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0002_customresultstable_number"),
    ]

    operations = [
        migrations.RemoveField(model_name="customresultstable", name="contests",),
    ]
