# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0006_auto_20151107_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='body',
            field=models.CharField(max_length=1000, default=datetime.datetime(2015, 11, 7, 10, 6, 48, 170883, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='quote',
            field=models.CharField(blank=True, max_length=100, default=datetime.datetime(2015, 11, 7, 10, 6, 56, 203264, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 11, 7, 10, 7, 4, 723302, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
