# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('academic_level', models.CharField(choices=[('Msc', 'Masters'), ('Bsc', 'Bachelor'), ('HF', 'Höhere Fachschule'), ('EFZ', 'Eidgenösisches Fähigkeits Zeugnis')], max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=100)),
                ('graduate_year', models.DateField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'ordering': ['-graduate_year'],
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('responsible', 'Employee with responsibilities'), ('leader', 'Team leader')], max_length=100)),
                ('employment_type', models.CharField(choices=[('fulltime', 'Fulltime'), ('parttime', 'Parttime'), ('freelancer', 'Freelancer')], max_length=100)),
                ('employer', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=500, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'ordering': ['-end_date'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('language', models.CharField(choices=[('english', 'English'), ('german', 'German'), ('french', 'French'), ('portuguese', 'Portuguese')], max_length=100)),
                ('level', models.CharField(choices=[('understand', 'Understand it'), ('speak', 'Understand and speak it'), ('fluent', 'fluent'), ('mother_tongue', 'mother tongue')], max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.SmallIntegerField(choices=[(1, 'I know what it is'), (2, 'I am a beginner at it'), (3, 'Good at it'), (4, 'I did advanced stuff with it'), (5, 'I am Pro in it')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
    ]
