# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0027_auto_20171209_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboardentry',
            name='last_submission_time',
        ),
    ]
