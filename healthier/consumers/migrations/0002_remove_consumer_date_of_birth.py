# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-18 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='date_of_birth',
        ),
    ]