# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_remove_experience_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='body',
            field=models.CharField(null=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='experience',
            name='title',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
