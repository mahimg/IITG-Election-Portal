# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 17:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda1', models.CharField(max_length=1000)),
                ('agenda2', models.CharField(max_length=1000)),
                ('agenda3', models.CharField(max_length=1000)),
                ('agenda4', models.CharField(max_length=1000)),
                ('vote_count', models.IntegerField(default=0)),
                ('pic', models.ImageField(height_field=400, upload_to='images/contestants/', width_field=300)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('voting_status', models.BooleanField(default=False)),
                ('category', models.IntegerField()),
            ],
        ),
    ]
