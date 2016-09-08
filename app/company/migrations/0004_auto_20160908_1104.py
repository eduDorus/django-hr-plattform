# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20160907_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='admins',
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=1500, null=True, blank=True),
        ),
    ]
