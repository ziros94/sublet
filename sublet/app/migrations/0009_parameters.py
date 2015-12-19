# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20151215_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(default=b'', max_length=200)),
                ('intercept', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sqFt_coef', models.DecimalField(max_digits=10, decimal_places=2)),
                ('year_coef', models.DecimalField(max_digits=10, decimal_places=2)),
                ('has_doorman_coef', models.DecimalField(max_digits=10, decimal_places=2)),
                ('min_from_subway_coef', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
