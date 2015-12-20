import django
from app.models import *
django.setup()

ApartmentOwned.objects.using('db3').filter(user_pk=2).delete()
ListingOwned.objects.using('db3').filter(user_pk=2).delete()
Parameters.objects.using('default').filter(city='new york').delete()
