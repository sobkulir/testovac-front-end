# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-09 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customresultstable",
            name="number",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
