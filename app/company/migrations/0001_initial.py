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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationProcess',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True, max_length=1500)),
                ('size', models.IntegerField(choices=[(10, '1 - 10'), (50, '11 - 50'), (100, '51 - 100'), (250, '101 - 250'), (500, '251 - 500'), (1000, '501 - 1000'), (10000, '1000 - 10000'), (100000, '10000 +')], null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True, max_length=250)),
                ('logo', models.ImageField(default='media/logos/default-logo.jpg', upload_to='logos')),
                ('permission_requests', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='permission_requests', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('degree', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1500)),
                ('employment_grade', models.PositiveIntegerField(choices=[(10, '10 %'), (20, '20 %'), (30, '30 %'), (40, '40 %'), (50, '50 %'), (60, '60 %'), (70, '70 %'), (80, '80 %'), (90, '90 %'), (100, '100 %')])),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('applications_process', models.ForeignKey(to='company.ApplicationProcess', on_delete=None)),
                ('company', models.ForeignKey(to='company.Company', on_delete=None)),
                ('min_degree', models.ForeignKey(to='company.Education', on_delete=None)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('earning', models.IntegerField(choices=[(35000, "35'000 - 50'000, (~3500 per month)"), (50000, "50'000 - 65'000, (~4800 per month)"), (65000, "65'000 - 80'000, (~6000 per month)"), (80000, "80'000 - 95'000, (~7300 per month)"), (100000, "100'000 - 125'000, (~9400 per month)"), (125000, "125'000 - 150'000, (~11'000 per month)")])),
                ('job', models.ForeignKey(to='company.Job', on_delete=None)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'The employee knows what it is'), (2, 'The employee is a beginner at it'), (3, 'The employee Good at it'), (4, 'The employee did advanced stuff with it'), (5, 'The employee is specialized in it')])),
                ('job', models.ForeignKey(to='company.Job', on_delete=None)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField(choices=[(1, 'The employee knows what it is'), (2, 'The employee is a beginner at it'), (3, 'The employee Good at it'), (4, 'The employee did advanced stuff with it'), (5, 'The employee is specialized in it')])),
                ('job', models.ForeignKey(to='company.Job', on_delete=None)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(null=True, to='company.Sector', on_delete=None, blank=True),
        ),
        migrations.AddField(
            model_name='applicationprocess',
            name='company',
            field=models.ForeignKey(to='company.Company'),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='application_process',
            field=models.ForeignKey(to='company.ApplicationProcess', on_delete=None),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='next',
            field=models.ForeignKey(null=True, to='company.ApplicationElement', related_query_name='next_field', related_name='next_field', blank=True),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='previous',
            field=models.ForeignKey(null=True, to='company.ApplicationElement', related_query_name='previous_field', related_name='previous_field', blank=True),
        ),
        migrations.AddField(
            model_name='applicationelement',
            name='queue',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
