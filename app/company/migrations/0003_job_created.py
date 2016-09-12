# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160912_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateField(default=datetime.datetime(2016, 9, 12, 13, 6, 30, 488702, tzinfo=utc), verbose_name=datetime.datetime(2016, 9, 12, 13, 6, 16, 911017, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
