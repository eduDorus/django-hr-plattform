# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('degree', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('employment_grade', models.PositiveIntegerField(choices=[(10, '10 %'), (20, '20 %'), (30, '30 %'), (40, '40 %'), (50, '50 %'), (60, '60 %'), (70, '70 %'), (80, '80 %'), (90, '90 %'), (100, '100 %')])),
                ('office', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('experience', models.PositiveSmallIntegerField()),
                ('level', models.PositiveSmallIntegerField()),
                ('job', models.ForeignKey(to='company.Job', on_delete=None)),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True, max_length=500),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(to='company.Company', on_delete=None),
        ),
        migrations.AddField(
            model_name='job',
            name='min_degree',
            field=models.ForeignKey(to='company.Education', on_delete=None),
        ),
    ]
