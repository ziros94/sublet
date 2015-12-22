 __author__      = "Alvi"
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


def main(n):
	listings = getListings()
	# print listings
	get_featureset(n, listings)

if __name__ == "__main__":
	main(10000)