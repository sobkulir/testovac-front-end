# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2020-03-18 12:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0008_auto_20200318_1310"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="contest",),
    ]
