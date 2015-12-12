# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151211_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='duration',
            field=models.IntegerField(default=1),
        ),
    ]
