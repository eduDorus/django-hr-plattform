# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20160915_1500'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('job', models.OneToOneField(to='company.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('process', models.ForeignKey(to='application.Process')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='queue',
            field=models.OneToOneField(to='application.Queue'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
