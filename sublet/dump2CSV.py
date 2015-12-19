__author__      = "Emily"
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
	writer = csv.writer(open("./support/dump.csv", 'w'))
	for record in qs_listing:
		header = ['sqFt','year','has_doorman','min_from_subway','price']	
		featureset[0] = header	
		listing_id = record[0]
		listing = ListingOwned.objects.get(pk=listing_id)
		apartment_id = listing.apartment.id
		'''
		right now we have one fake listing map to one apartment, but in real world scenario, it is possible (though rare) that within
		this recent 10K, there is more than one listings map to a single apartment, and this can cause heteroscedasticity to compromise
		the unbiasness of the regression model. The way to resolve this, is to create a dictionary with "apartment_id" as its key, 
		and "listing_id"(s) as the value. The program only looks for the max(lisiting_id) for each single key. 
		It is clear that the max(listing_id) is the latest listing for a particular apartment. 
		This step will increase processing time, and its requireness should be determined by the degree of heteroscedasticity of the current model with real-word data. 
		In the demo stage, it is determined as unnecesary to handle this. 
		'''
		apart_info_qs = ApartmentOwned.objects.filter(id=apartment_id).values_list('sqFt','year','has_doorman','min_from_subway')
		apart_info_list = list(apart_info_qs[0])
		#cast has_doorman: True to 1 and False to 0
		apart_info_list[2] = int(apart_info_list[2])
		apart_info_list.append(record[1])
		featureset[i] = apart_info_list
		i += 1
	writer.writerows(featureset)
			
def main(n):
	n = n
	city = "New York"
	'''
	since New York is the only city has enough data to form regression, we are only building regression model for New York in the demo stage
	in development, each city should have its regression model
	'''
	qs_listing = ListingOwned.objects.filter(apartment__city=city).values_list('id','price').order_by('id').reverse()[:n]
	get_featureset(n, qs_listing)
	
if __name__ == "__main__":
	main(10000)

