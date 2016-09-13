# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20160913_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='logos', default='media/logos/default-logo.jpg'),
        ),
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 13, 11, 21, 45, 839359, tzinfo=utc)),
        ),
    ]
