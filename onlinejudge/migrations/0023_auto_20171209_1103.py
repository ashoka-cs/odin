# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 11:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0022_leaderboardentry_last_submission_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboardentry',
            name='last_submission_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 9, 11, 3, 47, 501395)),
        ),
    ]
