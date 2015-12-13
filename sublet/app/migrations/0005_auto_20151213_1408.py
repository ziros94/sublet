# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151213_1346'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subletuser',
            unique_together=set([('user_pk', 'id')]),
        ),
    ]
