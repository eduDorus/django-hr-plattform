# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('company', models.ForeignKey(null=True, to='company.Company', blank=True, on_delete=None)),
            ],
        ),
    ]
