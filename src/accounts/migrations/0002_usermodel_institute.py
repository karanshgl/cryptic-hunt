# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-06 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='institute',
            field=models.CharField(default='NA', max_length=255),
        ),
    ]