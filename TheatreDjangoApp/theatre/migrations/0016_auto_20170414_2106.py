# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0015_auto_20170414_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='img',
            field=models.ImageField(default='post-img/default.jpg', upload_to='post-img/', verbose_name='Path to post-img'),
        ),
    ]
