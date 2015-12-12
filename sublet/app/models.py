from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Apartment(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    user = models.ForeignKey(User)


class Listing(models.Model):
    price = models.DecimalField(decimal_places=2)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=False)
    apartment = models.ForeignKey(Apartment)


class Booking(models.Model):
    duration = models.IntegerField()
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)


class OfferPlaced(models.Model):
    price = models.DecimalField(decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)


class OfferReceived(models.Model):
    price = models.DecimalField(decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)