# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151213_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerplaced',
            name='user_pk',
        ),
        migrations.RemoveField(
            model_name='offerreceived',
            name='user_pk',
        ),
    ]
