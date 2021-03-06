#10k row of apartment data 1-1 map to another 10k row of listing data
import django
import csv
from app.models import ListingOwned
from app.models import ApartmentOwned

django.setup()

def load_listing_data():
  with open('./support/listing_data.csv','r') as f:
    i = 40001
    reader = csv.reader(f)
    for row in reader:
      #the test apartment data starts with pk_40001 to pk_50000
      apartment = ApartmentOwned.objects.using('db3').get(pk=i)  
      i += 1
      apartment.listings_owned.create(
       		title = row[0], 
       		price = row[1], 
       		user_pk = row[2],
       		duration = row[3],
       		is_booked = row[4])
def main():
  load_listing_data()

if __name__ == "__main__":
    main()
#to view the results in file
#./manage.py dumpdata app.ListingOwned --indent 2 >./support/list_test.json      

 

