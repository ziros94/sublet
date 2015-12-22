from sharding import set_user_for_sharding, set_db_for_sharding, get_all_shards
import sys
import os
import django
cur = os.path.dirname(os.path.realpath('__file__'))
project_path = os.path.abspath(os.path.join(cur, os.pardir))
sys.path.append(project_path)
os.environ["DJANGO_SETTINGS_MODULE"] = "sublet.settings"
django.setup()
from app.models import ApartmentOwned, ListingOwned, SubletUser, User, ApartmentWanted, ListingWanted, BookingPlaced
from random import gauss, choice
import csv
from django.db.models import Q

def create_prices(num_apartments):
    prices = []
    for i in range(num_apartments):
        value = float(format(gauss(40, 15),'.2f'))
        while value < 0:
            value = float(format(gauss(40, 15),'.2f'))
        prices.append(value)
    prices.sort()
    print "Prices: " + str(prices)
    return prices


def create_sqfts(num_apartments):
    sqfts = []
    for i in range(num_apartments):
        value = float(int(round(gauss(700, 100))))
        while value < 0:
            value = float(int(gauss(700, 100)))
        sqfts.append(value)
    sqfts.sort()
    print "Sqfts " + str(sqfts)
    return sqfts

def create_years(num_apartments):
    years = []
    for i in range(num_apartments):
        value = int(round(gauss(1990, 7)))
        while value < 0:
            value = int(round(gauss(1990, 7)))
        years.append(value)
        years.sort()
    print "Years " + str(years)
    return years


def create_mins_from_subway(num_apartments):
    min_away = []
    for i in range(num_apartments):
        value = int(round(gauss(30, 20)))
        while value < 2:
            value = int(round(gauss(30, 20)))
        min_away.append(value)
        min_away.sort(reverse=True)
    # print "Minutes away " + str(min_away)
    return min_away


def createUsers():
    USERS = [
            {"username":"TestUser1", "email":"test1@test.com", "password": "1234", "first_name": "Tester1", "last_name": "Test"},
            {'username':"TestUser2", 'email':"test2@test.com", 'password': "1234", "first_name": "Tester2", "last_name": "Test"},
            {'username':"TestUser3", 'email':"test3@test.com", 'password': "1234", "first_name": "Tester3", "last_name": "Test"}
         ]
    for user in USERS:
        print user['username']
        new_user = User(username=user["username"], email=user["email"], first_name=user["first_name"], last_name=user["last_name"])
        new_user.set_password(user["password"])
        new_user.save()
        sublet_user = SubletUser(user_pk=new_user.id, username=new_user.username, first_name=new_user.first_name, last_name=new_user.last_name, email=new_user.email)
        sublet_user.save()

def getShardId():
    usernames = ["TestUser1","TestUser2","TestUser3"]
    rand_username = choice(usernames)
    user = User.objects.get(username=rand_username)
    # print user.id
    return user.id

def getSubletUser(id):
    user_query = SubletUser.objects
    set_user_for_sharding(user_query, id)
    user = user_query.get(user_pk=id)
    # print user
    return user

def getApartment(id):
    user_query = ApartmentOwned.objects
    set_user_for_sharding(user_query, id)
    apartment = choice(user_query.all())
    # print apartment
    return apartment

def createApartments(num_apartments):
    streets = ["Bayberry Drive","2nd Street","Poplar Street","5th Street South","Cedar Lane","Mulberry Lane","Locust Street","West Avenue","Augusta Drive","Lakeview Drive","Central Avenue","Heather Lane","Forest Street","Essex Court","Riverside Drive","7th Street","Edgewood Drive","Race Street","Fawn Lane","Division Street","Chapel Street","Washington Street","Summit Avenue","Highland Drive","Inverness Drive","Monroe Street","Redwood Drive","Willow Lane","Route 202","Cooper Street","Front Street North","Colonial Drive","Myrtle Street","1st Avenue","Valley View Drive","Harrison Street","Route 70","Water Street","Oak Lane","Euclid Avenue","Pheasant Run","B Street","Winding Way","Hillside Drive","Lilac Lane","Heather Court","Pennsylvania Avenue","Fairview Road","Hilltop Road","Cedar Street","Valley Road","Durham Court","Grove Street","4th Street","College Avenue","Manor Drive","Lexington Drive","Magnolia Court","Front Street","4th Street South","Hillcrest Drive","Sycamore Lane","12th Street","Andover Court","Orange Street","Route 11","Jefferson Street","Grove Avenue","Ivy Lane","Sherwood Drive","Old York Road","School Street","Canterbury Road","Locust Lane","Holly Drive","3rd Street West","Eagle Street","Vine Street","East Street","Walnut Avenue","Harrison Avenue","Rose Street","Route 7","Forest Avenue","Washington Avenue","Durham Road","Prospect Street","Howard Street","Hickory Lane","White Street","Walnut Street","Street Road","Mill Road","2nd Avenue","Route 32","Liberty Street","Adams Street","Cedar Court","Lake Avenue","Fulton Street"]
    sorted_sqfts = create_sqfts(num_apartments)
    sorted_years = create_years(num_apartments)
    sorted_mins = create_mins_from_subway(num_apartments)
    list_index = 0
    for i in range(num_apartments):
        list_index = 0 if list_index == len(streets)-1 else list_index+1
        id = getShardId()
        user = getSubletUser(id)
        sqFt = sorted_sqfts[i]
        year = sorted_years[i]
        min_from_subway = sorted_mins[i]
        apartment = ApartmentOwned(user_pk=id, street=streets[list_index], city='New York', state='NY', zip='10009', user=user, sqFt=sqFt, year=year, min_from_subway=min_from_subway)
        apartment.save()


def createListingsAndBookings(num_listings):
    sorted_prices = create_prices(num_listings)
    for i in range(num_listings):
        id = getShardId()
        apartment = getApartment(id)
        new_listing = ListingOwned(user_pk=id, title="Warning, this is for regression testing", price=sorted_prices[i], duration=30, apartment=apartment, is_booked=True, is_active=False)
        new_listing.save()
        # print new_listing
        a = new_listing.apartment
        s_user = getSubletUser(id)
        apartment_wanted = ApartmentWanted(user_pk=id, street=a.street, city=a.city, state=a.state, zip=a.zip, user=s_user, sqFt=a.sqFt, year=a.year, min_from_subway=a.min_from_subway)
        apartment_wanted.save()
        listing_wanted = ListingWanted(user_pk=id, title=new_listing.title, price=new_listing.price, duration=new_listing.duration, apartment=apartment_wanted)
        listing_wanted.save()
        booking_placed = BookingPlaced(user_pk=id, duration=listing_wanted.duration, listing=listing_wanted, user=s_user)
        booking_placed.save()
        print booking_placed

def createApartmentCSV():
    apartment_query = ApartmentOwned.objects
    shards = get_all_shards()
    apartments_owned = []
    users = User.objects.filter( Q(username="TestUser1") | Q(username="TestUser2") | Q(username="TestUser3") )
    # print users
    for shard in shards:
        set_db_for_sharding(apartment_query, shard)
        apartments_owned += apartment_query.filter( Q(user_pk=users[0].id) | Q(user_pk=users[1].id) | Q(user_pk=users[2].id) )
    apartments_owned = apartments_owned.order_by('sqFt')
    with open('apart_data.csv', 'wb') as fp:
        writer = csv.writer(fp, delimiter=',')
        for apartment in apartments_owned:
            row = [str(apartment.city),str(apartment.zip), str(apartment.sqFt), str(apartment.user_pk), str(apartment.min_from_subway), str(apartment.state), str(apartment.street), str(apartment.year)]
            writer.writerow(row)

def createListingCSV():
    listing_query = ListingOwned.objects
    shards = get_all_shards()
    listings_owned = []
    users = User.objects.filter( Q(username="TestUser1") | Q(username="TestUser2") | Q(username="TestUser3") )
    for shard in shards:
        set_db_for_sharding(listing_query, shard)
        listings_owned += listing_query.filter(Q(user_pk=users[0].id) | Q(user_pk=users[1].id) | Q(user_pk=users[2].id))
    listings_owned = listings_owned.order_by('price')
    with open('listing_data.csv','wb') as fp:
        writer = csv.writer(fp, delimiter=',')
        for listing in listings_owned:
            row = [str(listing.title), str(listing.price), str(listing.user_pk), str(listing.duration), str(int(listing.is_booked))]
            writer.writerow(row)

def editApartments():
    sorted_mins = create_mins_from_subway(10000)
    apartment_query = ApartmentOwned.objects
    shards = get_all_shards()
    users = User.objects.filter( Q(username="TestUser1") | Q(username="TestUser2") | Q(username="TestUser3") )
    apartments_owned = []
    for shard in shards:
        set_db_for_sharding(apartment_query, shard)
        apartments_owned += apartment_query.filter( Q(user_pk=users[0].id) | Q(user_pk=users[1].id) | Q(user_pk=users[2].id))
    # apartments_owned = apartments_owned.order_by('sqFt')
    print len(apartments_owned)
    apartments_owned.sort(key=lambda x: x.sqFt)
    for i in range(10000):
        # print apartments_owned[i]
        min_from_subway = sorted_mins[i]
        apartments_owned[i].min_from_subway = min_from_subway
        apartments_owned[i].save()
        print "another one"

def main(num_apartments, num_listings):
    # createUsers()
    # createApartments(num_apartments)
    # createListingsAndBookings(num_listings)
    # createApartmentCSV()
    # createListingCSV()
    editApartments()
if __name__ == '__main__':
    main(10000, 10000)