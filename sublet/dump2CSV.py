__author__      = "Emily"
#sklearn regression module takes in multinamentional array as the featureset, 
#which can be easily transformed through a csv with existing functions.
#in order to suffice that, we use this script to export Django queryset to csv. 
import csv
import os
import sys

import django

cur = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(cur)
os.environ["DJANGO_SETTINGS_MODULE"] = "sublet.settings"
django.setup()
from support.population import getListings


def get_featureset(n, listings):
    featureset = [[] for x in xrange(n+1)]

    with open("./support/dump.csv", 'wb') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerow(['sqFt','year','min_from_subway','price'])
        for listing in listings:
            apartment = listing.apartment
            row = [str(apartment.sqFt),str(apartment.year), str(apartment.min_from_subway), str(listing.price)]
            writer.writerow(row)
        '''
        [1]
        in deployment, don't know which db to query listings. Work around this using
        listing_query = ListingOwned.objects
        set_user_for_sharding(listing_query,user_pk=2)
        listing = listing_query.get(pk=listing_id)
        '''

        '''
        [2]
        right now we have one fake listing map to one apartment, but in real world scenario, it is possible (though rare) that within
        this recent 10K, there is more than one listings map to a single apartment, and this can cause heteroscedasticity to compromise
        the unbiasness of the regression model. The way to resolve this, is to create a dictionary with "apartment_id" as its key,
        and "listing_id"(s) as the value. The program only looks for the max(lisiting_id) for each single key.
        It is clear that the max(listing_id) is the latest listing for a particular apartment.
        This step will increase processing time, and its requireness should be determined by the degree of heteroscedasticity of the current model with real-word data.
        In the demo stage, it is determined as unnecesary to handle this.
        [3] dont know which db to query Apartments? same as [1] resolve using set_user_for_sharding
        '''


def main(n):
    '''
    [4]
    since New York is the only city has enough data to form regression, we are only building regression model for New York in the demo stage
    in development, each city should have its regression model
    [5] don't know which db to query listings? same as [1] resolve it by using set_user_for_sharding
    '''
    listings = getListings()
    # print listings
    get_featureset(n, listings)

if __name__ == "__main__":
    main(10000)

