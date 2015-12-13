from django.contrib import admin
from .models import ApartmentOwned, ApartmentWanted, ListingOwned, ListingWanted, BookingReceived, BookingPlaced, OfferPlaced, OfferReceived, SubletUser
# Register your models here.

admin.site.register(ApartmentOwned)
admin.site.register(ApartmentWanted)

admin.site.register(ListingOwned)
admin.site.register(ListingWanted)
admin.site.register(BookingReceived)
admin.site.register(BookingPlaced)
admin.site.register(OfferPlaced)
admin.site.register(OfferReceived)
admin.site.register(SubletUser)