from app.models import ApartmentOwned
from app.models import SubletUser
user = SubletUser.objects.get(pk=11)
print(dir(ApartmentOwned))
#test = user.apartments_owned.create(city='New York', zip='10009',sqFt='100',has_doorman='true', user_pk=11,min_from_subway=5, #state='NY',street='14th street',year=1940)