# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackaccess',
            name='PrimaryTrack',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='start.Track'),
        ),
    ]
