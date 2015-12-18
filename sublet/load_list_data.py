#10k row of apartment data 1-1 map to another 10k row of listing data
import django
import csv
from app.models import ListingOwned
from app.models import ApartmentOwned

django.setup()

def load_list_data():
  with open('list_data.csv','r') as f:
    i = 20002
    reader = csv.reader(f)
    for row in reader:
      #the test apartment data starts with pk_20002 to pk_30001
      apartment = ApartmentOwned.objects.get(pk=i)  
      i += 1
      apartment.listings_owned.create(
       		title = row[0], 
       		price = row[1], 
       		is_active = row[2],
       		user_pk = row[3],
       		duration = row[4],
       		is_booked = row[5])
def main():
  load_list_data()

if __name__ == "__main__":
    main()
#to view the results in file
#./manage.py dumpdata app.ListingOwned --indent 2 > list_test.json      

 

