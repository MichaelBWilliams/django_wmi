# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-19 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20170414_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='map',
            options={'permissions': (('KE', 'Kenya Permission'),)},
        ),
    ]
