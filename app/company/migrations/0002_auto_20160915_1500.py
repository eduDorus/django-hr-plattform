# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationelement',
            name='application_process',
        ),
        migrations.RemoveField(
            model_name='applicationelement',
            name='next',
        ),
        migrations.RemoveField(
            model_name='applicationelement',
            name='previous',
        ),
        migrations.RemoveField(
            model_name='applicationelement',
            name='queue',
        ),
        migrations.RemoveField(
            model_name='applicationprocess',
            name='company',
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='media/logos/default-logo.jpg', upload_to='media/logos'),
        ),
        migrations.AlterField(
            model_name='job',
            name='applications_process',
            field=models.ForeignKey(on_delete=None, to='application.Process'),
        ),
        migrations.DeleteModel(
            name='ApplicationElement',
        ),
        migrations.DeleteModel(
            name='ApplicationProcess',
        ),
    ]
