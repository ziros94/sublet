#these data are under user_pk = 2
import csv
from random import gauss

def get_price(n):
    n = n
    price = []
    while len(price) < n:
        value = gauss(50, 10)
        value = format(value, '.2f')
        price.append(value)
    price.sort(key=lambda p: float(p))
    return price

def get_title(n):
	n = n
	title = []
	while len(title) < n:
		value = "Warning, this is for regression testing"
		title.append(value)
	return title

def get_user_pk(n):
	n = n
	pk = []
	while len(pk) < n:
		value = 2
		pk.append(value)
	return pk

def duration(n):
	n = n
	days = []
	while len(days) < n:
		value = 30
		days.append(value)
	return days

def get_booked(n):
	n = n
	is_booked = []
	while len(is_booked) < n:
		value = 1
		is_booked.append(value)
	return is_booked

def main(n):
    n = n
    price = get_price(n)
    title = get_title(n)
    user_pk = get_user_pk(n)
    days = duration(n)
    booked = get_booked(n)
    featureset = [[] for x in xrange(n)]
    #featureset[0]= ["apartment", "title", "price","user_pk", "duration", "is_booked"]
    feature_entry = []
    for i in range(n):
        feature_entry.append(title[i])
        feature_entry.append(price[i])
        feature_entry.append(user_pk[i])
        feature_entry.append(days[i])
        feature_entry.append(booked[i])
        featureset[i] = feature_entry
        feature_entry = []        
    with open('listing_data.csv','w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(featureset)
        
if __name__ == "__main__":
    main(10000)
