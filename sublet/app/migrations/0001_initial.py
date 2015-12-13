# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentOwned',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentWanted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='BookingPlaced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('duration', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BookingReceived',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('duration', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ListingOwned',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('title', models.CharField(default=b'', max_length=200)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('duration', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('apartment', models.ForeignKey(related_name='listings_owned', to='app.ApartmentOwned')),
            ],
        ),
        migrations.CreateModel(
            name='ListingWanted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('title', models.CharField(default=b'', max_length=200)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('duration', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('apartment', models.ForeignKey(related_name='listings_wanted', to='app.ApartmentWanted')),
            ],
        ),
        migrations.CreateModel(
            name='OfferPlaced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('is_accepted', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('listing', models.ForeignKey(to='app.ListingOwned')),
            ],
        ),
        migrations.CreateModel(
            name='OfferReceived',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('is_accepted', models.BooleanField(default=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('listing', models.ForeignKey(to='app.ListingOwned')),
            ],
        ),
        migrations.CreateModel(
            name='SubletUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_pk', models.PositiveIntegerField()),
                ('username', models.CharField(max_length=254)),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='offerreceived',
            name='user',
            field=models.ForeignKey(related_name='offers_received', to='app.SubletUser'),
        ),
        migrations.AddField(
            model_name='offerplaced',
            name='user',
            field=models.ForeignKey(related_name='offers_placed', to='app.SubletUser'),
        ),
        migrations.AddField(
            model_name='bookingreceived',
            name='listing',
            field=models.ForeignKey(to='app.ListingOwned'),
        ),
        migrations.AddField(
            model_name='bookingreceived',
            name='user',
            field=models.ForeignKey(related_name='bookings_received', to='app.SubletUser'),
        ),
        migrations.AddField(
            model_name='bookingplaced',
            name='listing',
            field=models.ForeignKey(to='app.ListingWanted'),
        ),
        migrations.AddField(
            model_name='bookingplaced',
            name='user',
            field=models.ForeignKey(related_name='bookings_placed', to='app.SubletUser'),
        ),
        migrations.AddField(
            model_name='apartmentwanted',
            name='user',
            field=models.ForeignKey(related_name='apartments_wanted', to='app.SubletUser'),
        ),
        migrations.AddField(
            model_name='apartmentowned',
            name='user',
            field=models.ForeignKey(related_name='apartments_owned', to='app.SubletUser'),
        ),
    ]
