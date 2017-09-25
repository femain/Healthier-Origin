# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20170924_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedservice',
            name='service_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basehealthierservice',
            name='service_id',
            field=models.CharField(default='service_40enwk5ew3pmc2g0unon', max_length=200),
        ),
        migrations.AlterField(
            model_name='orderedservice',
            name='order_id',
            field=models.CharField(default='order_8qfaytkhajpgqgq70yht', max_length=200),
        ),
    ]
