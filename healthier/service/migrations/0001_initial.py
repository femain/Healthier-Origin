# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 06:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_prices.models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseHealthierService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('details', models.CharField(default='', max_length=1000)),
                ('price', django_prices.models.PriceField(currency='NGN', decimal_places=2, max_digits=12)),
                ('service_id', models.CharField(default='service_bbon1gs9cs4t1m0xgzus', max_length=200)),
                ('days_available', models.CharField(choices=[('EVERYDAY', 'EVR'), ('MONDAYS', 'MON'), ('TUESDAYS', 'TUE'), ('WEDNESDAYS', 'WED'), ('THURSDAYS', 'THU'), ('FRIDAYS', 'FRI'), ('SATURDAYS', 'SAT'), ('SUNDAYS', 'SUN')], max_length=200)),
                ('time_available', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeasuredTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lower_range', models.CharField(max_length=200)),
                ('upper_range', models.CharField(max_length=200)),
                ('measure_value', models.CharField(max_length=200)),
                ('measured_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('measured_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumers.Consumer')),
                ('service_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(blank=True, choices=[('', 'Payment Status'), ('Paid', 'P'), ('Not Paid', 'NP')], max_length=200)),
                ('order_id', models.CharField(default='order_6vt1r3euu6x2i36carua', max_length=200)),
                ('preferred_date', models.DateField(default=(('EVERYDAY', 'EVR'), ('MONDAYS', 'MON'), ('TUESDAYS', 'TUE'), ('WEDNESDAYS', 'WED'), ('THURSDAYS', 'THU'), ('FRIDAYS', 'FRI'), ('SATURDAYS', 'SAT'), ('SUNDAYS', 'SUN')))),
                ('preferred_time', models.CharField(max_length=200)),
                ('promo_code', models.CharField(max_length=200)),
                ('order_date', models.DateTimeField()),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumers.Consumer')),
                ('provided_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('group_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceGroupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_fields', jsonfield.fields.JSONField()),
                ('generated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_sent', models.BooleanField(default=False)),
                ('file_upload', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/')),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroup')),
                ('service_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.BaseHealthierService')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceReportGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('group_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField()),
                ('request_type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=200)),
                ('healthier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumers.Consumer')),
            ],
        ),
        migrations.AddField(
            model_name='servicegroup',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroupCategory'),
        ),
        migrations.AddField(
            model_name='basehealthierservice',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.ServiceGroup'),
        ),
        migrations.AddField(
            model_name='basehealthierservice',
            name='provider_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='providers.Provider'),
        ),
    ]
