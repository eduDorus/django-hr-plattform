# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0006_auto_20160908_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='applications',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
