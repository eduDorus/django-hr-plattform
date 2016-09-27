# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20160915_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='motivation',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
