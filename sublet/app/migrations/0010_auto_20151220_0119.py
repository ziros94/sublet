# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_parameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentowned',
            name='has_doorman',
        ),
        migrations.RemoveField(
            model_name='apartmentwanted',
            name='has_doorman',
        ),
        migrations.RemoveField(
            model_name='listingowned',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='listingwanted',
            name='is_active',
        ),
    ]
