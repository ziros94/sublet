# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151213_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listingowned',
            name='title',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='listingwanted',
            name='title',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
