# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0014_auto_20170414_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='img',
            field=models.ImageField(default='media/post-img/default.jpg', upload_to='media/post-img/', verbose_name='Path to post-img'),
        ),
    ]
