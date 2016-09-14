# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20160913_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'The employee knows what it is'), (2, 'The employee is a beginner at it'), (3, 'The employee Good at it'), (4, 'The employee did advanced stuff with it'), (5, 'The employee is specialized in it')])),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='experience',
        ),
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 9, 14, 8, 16, 21, 980187, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'The employee knows what it is'), (2, 'The employee is a beginner at it'), (3, 'The employee Good at it'), (4, 'The employee did advanced stuff with it'), (5, 'The employee is specialized in it')]),
        ),
        migrations.AddField(
            model_name='task',
            name='job',
            field=models.ForeignKey(on_delete=None, to='company.Job'),
        ),
    ]
