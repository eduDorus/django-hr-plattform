# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationProcess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1500, null=True, blank=True)),
                ('size', models.IntegerField(choices=[(10, '1 - 10'), (50, '11 - 50'), (100, '51 - 100'), (250, '101 - 250'), (500, '251 - 500'), (1000, '501 - 1000'), (10000, '1000 - 10000'), (100000, '10000 +')], null=True, blank=True)),
                ('website', models.URLField(max_length=250, null=True, blank=True)),
                ('permission_requests', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='permission_requests')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('degree', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1500)),
                ('employment_grade', models.PositiveIntegerField(choices=[(10, '10 %'), (20, '20 %'), (30, '30 %'), (40, '40 %'), (50, '50 %'), (60, '60 %'), (70, '70 %'), (80, '80 %'), (90, '90 %'), (100, '100 %')])),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('applications', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('applications_process', models.ForeignKey(on_delete=None, to='company.ApplicationProcess')),
                ('company', models.ForeignKey(on_delete=None, to='company.Company')),
                ('min_degree', models.ForeignKey(on_delete=None, to='company.Education')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('experience', models.PositiveSmallIntegerField()),
                ('level', models.PositiveSmallIntegerField()),
                ('job', models.ForeignKey(on_delete=None, to='company.Job')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(null=True, to='company.Sector', blank=True, on_delete=None),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='application_process',
            field=models.ForeignKey(on_delete=None, to='company.ApplicationProcess'),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='queue',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
