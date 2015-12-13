# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentowned',
            name='has_doorman',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartmentowned',
            name='min_from_subway',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartmentowned',
            name='sqFt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='apartmentowned',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartmentwanted',
            name='has_doorman',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='apartmentwanted',
            name='min_from_subway',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='apartmentwanted',
            name='sqFt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='apartmentwanted',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
