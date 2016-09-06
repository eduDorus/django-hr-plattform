# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(null=True, blank=True)),
                ('size', models.IntegerField(null=True, blank=True, choices=[(10, '1 - 10'), (50, '11 - 50'), (100, '51 - 100'), (250, '101 - 250'), (500, '251 - 500'), (1000, '501 - 1000'), (10000, '1000 - 10000'), (100000, '10000 +')])),
                ('website', models.URLField(null=True, blank=True, max_length=250)),
                ('admins', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='admins')),
                ('permission_requests', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='permission_requests')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(on_delete=None, null=True, blank=True, to='company.Sector'),
        ),
    ]
