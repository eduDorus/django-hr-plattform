# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationelement',
            name='next',
            field=models.ForeignKey(related_name='next_field', to='company.ApplicationElement', related_query_name='next_field', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationelement',
            name='previous',
            field=models.ForeignKey(related_name='previous_field', to='company.ApplicationElement', related_query_name='previous_field', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='applicationelement',
            name='queue',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='permission_requests',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='permission_requests', blank=True),
        ),
    ]
