# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20160914_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
