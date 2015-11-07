# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0004_experience_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='creation_date',
        ),
    ]
