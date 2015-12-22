__author__      = "Emily"
#depreciated, using Alvi's modified dump2CSV.py instead
#sklearn regression module takes in multinamentional array as the featureset, 
#which can be easily transformed through a csv with existing functions.
#in order to suffice that, we use this script to export Django queryset to csv. 
import django
import sys
import csv
from app.sharding import set_user_for_sharding
from django.db.models.loading import get_model
from app.models import ListingOwned
from app.models import ApartmentOwned
#10k under user_pk = 2 
django.setup()
reload(sys)  
sys.setdefaultencoding('utf-8')

def get_featureset(n,qs):
    n = n
    qs_listing = qs
    featureset = [[] for x in xrange(n+1)]
    #find matching apartment through listing
    i = 1
    writer = csv.writer(open("./support/dump.csv", 'w'))
    '''
        right now we have one fake listing map to one apartment, but in real world scenario, it is possible (though rare) that within
        this recent 10K, there is more than one listings map to a single apartment, and this can cause heteroscedasticity to compromise
        the unbiasness of the regression model. The way to resolve this, is to create a dictionary with "apartment_id" as its key, 
        and "listing_id"(s) as the value. The program only looks for the max(lisiting_id) for each single key. 
        It is clear that the max(listing_id) is the latest listing for a particular apartment. 
        This step will increase processing time, and its requireness should be determined by the degree of heteroscedasticity of the current model with real-word data. 
        In the demo stage, it is determined as unnecesary to handle this. 
    '''
    for record in qs_listing:
        header = ['sqFt','year','min_from_subway','price']
        featureset[0] = header
        listing_id = record[0]     
        listing_query = ListingOwned.objects
        set_user_for_sharding(listing_query,2)
        listing = listing_query.get(id=listing_id)       
        apartment_id = listing.apartment_id
        apart_query = ApartmentOwned.objects
        set_user_for_sharding(apart_query, 2)
        apart_info_qs = apart_query.filter(id=apartment_id).values_list('sqFt','year','min_from_subway')
        #apart_info_qs = ApartmentOwned.objects.using('db3').filter(id=apartment_id).values_list('sqFt','year','min_from_subway')
        apart_info_list = list(apart_info_qs[0])
        apart_info_list.append(record[1])
        featureset[i] = apart_info_list
        i += 1
    writer.writerows(featureset)

def main(n):
    n = n
    city = "New York"
    listing_query = ListingOwned.objects
    set_user_for_sharding(listing_query,2)
    qs_listing = listing_query.filter(apartment__city=city).values_list('id','price').order_by('id').reverse()[:n]
    #qs_listing = ListingOwned.objects.using('db3').filter(apartment__city=city, is_booked = 1).values_list('id','price').order_by('id').reverse()[:n]
    get_featureset(n, qs_listing)

if __name__ == "__main__":
    main(10000)

