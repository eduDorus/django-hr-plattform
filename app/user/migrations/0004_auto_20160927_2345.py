# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_profile_motivation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SocialProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='social_provider',
            field=models.ForeignKey(to='user.SocialProvider'),
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
