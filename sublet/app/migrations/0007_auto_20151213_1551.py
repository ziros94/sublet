# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20151213_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingowned',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listingwanted',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
