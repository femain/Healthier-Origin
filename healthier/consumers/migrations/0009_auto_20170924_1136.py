# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0008_auto_20170924_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='healthier_id',
            field=models.CharField(default='consumer_h9h74zxwj60kgkwvjdq7', max_length=30),
        ),
    ]
