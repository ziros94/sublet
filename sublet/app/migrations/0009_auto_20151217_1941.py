# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151215_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentowned',
            name='user',
        ),
        migrations.RemoveField(
            model_name='apartmentwanted',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bookingplaced',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='bookingplaced',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bookingreceived',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='bookingreceived',
            name='user',
        ),
        migrations.RemoveField(
            model_name='listingowned',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='listingwanted',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='offerplaced',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='offerplaced',
            name='user',
        ),
        migrations.RemoveField(
            model_name='offerreceived',
            name='listing',
        ),
        migrations.RemoveField(
            model_name='offerreceived',
            name='user',
        ),
    ]
