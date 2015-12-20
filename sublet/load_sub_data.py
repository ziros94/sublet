import django
import csv
from app.models import ApartmentOwned
from app.models import SubletUser

django.setup()

user = SubletUser.objects.using('db3').get(pk=2)
with open('./support/sub_data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
    	user.apartments_owned.create(
       		city = row[0],
       		zip = row[1],
       		sqFt = row[2],
       		user_pk = row[3],
       		min_from_subway = row[4],
       		state = row[5],
       		street = row[6],
       		year = row[7]
       	)

#./manage.py dumpdata app.ApartmentOwned --indent 2 >./support/apart_test.json
      
