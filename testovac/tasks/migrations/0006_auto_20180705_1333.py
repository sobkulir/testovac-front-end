# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-05 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_remove_contest_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="competition",
            name="slug",
            field=models.SlugField(
                help_text='Must be unique, serves as part of URL.<br />Must only contain characters "a-zA-Z0-9_-".',
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="contest",
            name="slug",
            field=models.SlugField(
                help_text='Must be unique among all contests, serves as part of URL.<br />Must only contain characters "a-zA-Z0-9_-".',
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="slug",
            field=models.SlugField(
                help_text='Must be unique among all tasks, serves as part of URL.<br />By default, task.slug is also used as a name of inputs folder at judge.<br />Must only contain characters "a-zA-Z0-9_-".',
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
