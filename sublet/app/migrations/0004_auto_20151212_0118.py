# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20151211_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerplaced',
            name='user',
            field=models.ForeignKey(related_name='offers_placed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offerreceived',
            name='user',
            field=models.ForeignKey(related_name='offers_received', to=settings.AUTH_USER_MODEL),
        ),
    ]
