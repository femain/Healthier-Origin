# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 06:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='user_details_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='consumer_details', to=settings.AUTH_USER_MODEL),
        ),
    ]
