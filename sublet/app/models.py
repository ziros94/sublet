from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Apartment(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{street},{city},{state} {zip}".format(street=self.street, city=self.city, state=self.state, zip=self.zip)


class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    is_active = models.BooleanField(default=False)
    apartment = models.ForeignKey(Apartment)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Booking(models.Model):
    duration = models.IntegerField()
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)


class OfferPlaced(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Offer  for {list_id}".format(title=self.listing.id)


class OfferReceived(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing)
    user = models.ForeignKey(User)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Offer  for {list_id}".format(title=self.listing.id)