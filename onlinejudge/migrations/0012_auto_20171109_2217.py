# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0011_problem_no_of_cases'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='no_of_cases',
            new_name='no_of_test_cases',
        ),
    ]