# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deadmanapp', '0004_auto_20160121_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('PHONE', 'Phone Number'), ('EMAIL', 'Email Address')], max_length=50),
        ),
        migrations.DeleteModel(
            name='ContactType',
        ),
    ]
