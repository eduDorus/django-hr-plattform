# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(to='company.Job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='queue',
            field=models.ForeignKey(to='application.Queue'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
