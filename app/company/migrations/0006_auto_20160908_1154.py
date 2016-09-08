# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20160908_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
