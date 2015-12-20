# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151220_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='has_doorman_coef',
        ),
    ]
