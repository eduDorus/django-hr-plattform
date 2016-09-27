# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20160927_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='icon',
            field=models.CharField(max_length=50, default='inbox'),
            preserve_default=False,
        ),
    ]
