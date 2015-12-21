# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151221_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingowned',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='listingwanted',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
