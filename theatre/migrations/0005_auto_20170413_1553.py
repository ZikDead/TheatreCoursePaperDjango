# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0004_hall_perfomance_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['-time_start'],
                'verbose_name_plural': 'Program',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_of_ticket', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tittle', models.CharField(max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='program',
            name='hall',
        ),
        migrations.RemoveField(
            model_name='program',
            name='perfomance',
        ),
        migrations.AlterModelOptions(
            name='hall',
            options={'verbose_name_plural': 'Halls'},
        ),
        migrations.RemoveField(
            model_name='hall',
            name='description_of_hall',
        ),
        migrations.AddField(
            model_name='hall',
            name='number_of_hall',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Perfomance',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.AddField(
            model_name='eventlist',
            name='hall',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theatre.Hall'),
        ),
        migrations.AddField(
            model_name='eventlist',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.Performance'),
        ),
    ]
