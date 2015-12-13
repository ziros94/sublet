from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class SubletUser(models.Model):
    user_pk = models.PositiveIntegerField()
    username = models.CharField(max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.username

class ApartmentOwned(models.Model):
    user_pk = models.PositiveIntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    user = models.ForeignKey(SubletUser, related_name='apartments_owned')

    def __str__(self):
        return "{street},{city},{state} {zip}".format(street=self.street, city=self.city, state=self.state, zip=self.zip)


class ApartmentWanted(models.Model):
    user_pk = models.PositiveIntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    user = models.ForeignKey(SubletUser, related_name='apartments_wanted')

    def __str__(self):
        return "{street},{city},{state} {zip}".format(street=self.street, city=self.city, state=self.state, zip=self.zip)


class ListingOwned(models.Model):
    user_pk = models.PositiveIntegerField()
    title = models.CharField(max_length=200,default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)
    apartment = models.ForeignKey(ApartmentOwned, related_name='listings_owned')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_owner(self, user):
        return self.apartment.user.user_pk == user.id


class ListingWanted(models.Model):
    user_pk = models.PositiveIntegerField()
    title = models.CharField(max_length=200,default="")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)
    apartment = models.ForeignKey(ApartmentWanted, related_name='listings_wanted')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_owner(self, user):
        return self.apartment.user == user


class BookingReceived(models.Model):
    user_pk = models.PositiveIntegerField()
    duration = models.IntegerField()
    listing = models.ForeignKey(ListingOwned)
    user = models.ForeignKey(SubletUser, related_name='bookings_received')
    date = models.DateField(default=timezone.now)


class BookingPlaced(models.Model):
    user_pk = models.PositiveIntegerField()
    duration = models.IntegerField()
    listing = models.ForeignKey(ListingWanted)
    user = models.ForeignKey(SubletUser, related_name='bookings_placed')
    date = models.DateField(default=timezone.now)


class OfferPlaced(models.Model):
    user_pk = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(ListingOwned)
    user = models.ForeignKey(SubletUser, related_name='offers_placed')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Offer placed for {list_title}".format(list_title=self.listing.title)


class OfferReceived(models.Model):
    user_pk = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_accepted = models.BooleanField(default=False)
    listing = models.ForeignKey(ListingOwned)
    user = models.ForeignKey(SubletUser, related_name='offers_received')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Offer received for {list_title}".format(list_title=self.listing.title)