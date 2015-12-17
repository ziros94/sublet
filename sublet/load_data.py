import django
django.setup()
import csv
from app.models import ApartmentOwned
from app.models import SubletUser

user = SubletUser.objects.get(pk=2)
with open('sub_data.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
    	user.apartments_owned.create(
       		city = row[0],zip = row[1],sqFt = row[2],has_doorman = row[3],user_pk = row[4],min_from_subway = row[5],state = row[6],street = row[7],year = row[8]
       	)
      

#import csv data to ApartmentOwned under user_pk =11
#to run this, might need to pass the environmental path by pasting the following to the terminal
