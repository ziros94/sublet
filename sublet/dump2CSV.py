#sklearn regression module takes in multinamentional array as the featureset, 
#which can be easily transformed through a csv with existing functions.
#in order to suffice that, we use this script to export Django queryset to csv. 
import csv
import sys
from django.db.models.loading import get_model
from app.models import ListingOwned
from app.models import ApartmentOwned
import django
django.setup()
reload(sys)  
sys.setdefaultencoding('utf-8')
'''

def dump(qs, outfile_path, n):   
	qs_sub  = qs
	writer = csv.writer(open(outfile_path, 'w'))
	featureset = [[] for x in xrange(n)]
	
	for i in range(n):
		feature_entry=list(qs[i])
		feature_entry[3] = int(feature_entry[3])
		featureset[i] = feature_entry
	writer.writerows(featureset)	
'''
#make sure the apartment data and price data are aligned
'''
def get_price(qs):
	qs_apart_id = qs
	price = []
	for apart_id in qs_apart_id:
    	apartment = ApartmentOwned.objects.get(pk=apart_id)   	
    	price.append(apartment.)
    	'''
'''
with open('list_data.csv','r') as f:
    reader = csv.reader(f)
    for i in range(10000):
    	#the test apartment data starts with pk_20002 to pk_30001
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
'''
def get_featureset(n,qs):
	n = n
	qs_listing = qs
	#find the latest list for the same apartment
	for record in qs_listing:
		
		listing_id = record[0]
		listing = ListingOwned.objects.get(pk=listing_id)
		print listing.apartment.id

			
def main(n):
	n = n
	#return the most recent n=10,000 rows
	#qs_sub = ApartmentOwned.objects.filter(city="New York").values_list('sqFt','year','has_doorman','min_from_subway').order_by('id').reverse()[:n]
	#qs_apart_id = ApartmentOwned.objects.filter(city="New York").values_list('id', flat=True).reverse()[:n]
	#print qs_apart_id
	qs_listing = ListingOwned.objects.filter(apartment__city="New York").values_list('id','price').order_by('id').reverse()[:n]

	print type(qs_listing)
	get_featureset(n, qs_listing)
	#get_price(qs_apart_id)
	#dump(qs_sub,"./dump.csv", n)
	
if __name__ == "__main__":
	main(2)
