# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0012_auto_20171109_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='language',
            field=models.CharField(choices=[['py', 'Python 3'], ['cpp', 'C++'], ['c', 'C']], default='py', max_length=20),
        ),
    ]
