# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_experience_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 7, 50, 52, 850314, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
