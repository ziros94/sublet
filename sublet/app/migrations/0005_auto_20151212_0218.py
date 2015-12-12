# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151212_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(related_name='apartments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listing',
            name='apartment',
            field=models.ForeignKey(related_name='listings', to='app.Apartment'),
        ),
    ]
