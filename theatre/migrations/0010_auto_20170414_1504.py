# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0009_auto_20170413_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventlist',
            options={'ordering': ['-date', '-time_start'], 'verbose_name_plural': 'EventList'},
        ),
        migrations.AlterModelManagers(
            name='eventlist',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='performance',
            name='img',
            field=models.ImageField(null=True, upload_to='static/img/', verbose_name='Path to post-img'),
        ),
    ]
