# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='problem_title',
            field=models.CharField(default='John', max_length=30),
            preserve_default=False,
        ),
    ]
