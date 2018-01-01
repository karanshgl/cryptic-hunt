# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-01 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_level_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_banned', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('current_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questions.Level')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]