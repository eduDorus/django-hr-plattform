# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_job_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(verbose_name=datetime.datetime(2016, 9, 13, 10, 47, 3, 761640, tzinfo=utc)),
        ),
    ]
