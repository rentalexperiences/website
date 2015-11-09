# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('quote', models.CharField(max_length=100, blank=True)),
                ('image', models.ImageField(null=True, upload_to='', blank=True)),
                ('negative', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('friendly_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='real_estate',
            field=models.ForeignKey(to='experiences.RealEstate'),
        ),
    ]
