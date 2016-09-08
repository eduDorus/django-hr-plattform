# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20160908_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 8, 11, 54, 8, 378506, tzinfo=utc)),
        ),
    ]
