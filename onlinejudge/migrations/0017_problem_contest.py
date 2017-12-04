# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0016_auto_20171128_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinejudge.Contest'),
            preserve_default=False,
        ),
    ]
