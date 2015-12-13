# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151213_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerplaced',
            name='user_pk',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='offerreceived',
            name='user_pk',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
