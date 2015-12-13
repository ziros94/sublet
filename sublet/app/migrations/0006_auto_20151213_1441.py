# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151213_1408'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subletuser',
            unique_together=set([]),
        ),
    ]
