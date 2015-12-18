import django
import csv
from app.models import ListingOwned
from app.models import ApartmentOwned

django.setup()

with open('list_data.csv','r') as f:
    reader = csv.reader(f)
    for i in range(10000):
    	apartment = ApartmentOwned.objects.get(pk=(i+20002))   	
    	for row in reader:
    		apartment.listings_owned.create(
       			title = row[0], 
       			price = row[1], 
       			is_active = row[2],
       			user_pk = row[3],
       			duration = row[4],
       			is_booked = row[5]
       	)

#./manage.py dumpdata app.ListingOwned --indent 2 > list_test.json      

