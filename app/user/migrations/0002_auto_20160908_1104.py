# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20160908_1104'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='company_user',
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(on_delete=None, blank=True, to='company.Company', null=True),
        ),
    ]
