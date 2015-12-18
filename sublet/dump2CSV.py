#sklearn regression module takes in multinamentional array as the featureset, 
#which can be easily transformed through a csv with existing functions.
#in order to suffice that, we use this script to export Django queryset to csv. 
import django
import sys
import csv
from django.db.models.loading import get_model
from app.models import ListingOwned
from app.models import ApartmentOwned

django.setup()
reload(sys)  
sys.setdefaultencoding('utf-8')

def get_featureset(n,qs):
	n = n
	qs_listing = qs
	featureset = [[] for x in xrange(n+1)]
	#find the latest list for the same apartment
	i = 1
	writer = csv.writer(open("./dump.csv", 'w'))
	for record in qs_listing:
		header = ['sqFt','year','has_doorman','min_from_subway','price']	
		featureset[0] = header	
		listing_id = record[0]
		listing = ListingOwned.objects.get(pk=listing_id)
		apartment_id = listing.apartment.id
		apart_info_qs = ApartmentOwned.objects.filter(id=apartment_id).values_list('sqFt','year','has_doorman','min_from_subway')
		apart_info_list = list (apart_info_qs[0])
		apart_info_list[2] = int(apart_info_list[2])
		apart_info_list.append(record[1])
		featureset[i] = apart_info_list
		i += 1
	writer.writerows(featureset)
			
def main(n):
	n = n
	qs_listing = ListingOwned.objects.filter(apartment__city="New York").values_list('id','price').order_by('id').reverse()[:n]
	get_featureset(n, qs_listing)
	
if __name__ == "__main__":
	main(10000)
