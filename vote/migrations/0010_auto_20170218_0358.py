# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0009_auto_20170217_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='pic',
            field=models.CharField(max_length=1000),
        ),
    ]