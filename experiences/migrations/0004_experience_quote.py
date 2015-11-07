# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0003_experience_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='quote',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
