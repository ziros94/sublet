from django.contrib import admin
from .models import  Apartment, Listing, Booking, OfferPlaced, OfferReceived
# Register your models here.

admin.site.register(Apartment)
admin.site.register(Listing)
admin.site.register(Booking)
admin.site.register(OfferPlaced)
admin.site.register(OfferReceived)