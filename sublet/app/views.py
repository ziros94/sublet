from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import ApartmentOwned, ApartmentWanted, ListingOwned, ListingWanted, BookingReceived, BookingPlaced, OfferPlaced, OfferReceived, SubletUser, User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from sharding import set_user_for_sharding, set_db_for_sharding, get_all_shards
from itertools import chain
from django.core.serializers.json import DjangoJSONEncoder
from support.estimated_price import getEstimatedPrice


import json
def home(request):
    return render(request, 'app/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.save()
        sublet_user = SubletUser(user_pk=new_user.id, username=new_user.username, first_name=new_user.first_name, last_name=new_user.last_name, email=new_user.email)
        sublet_user.save()
        print "New User Registered"
        return redirect('/sublet/')
    else:
        return render(request, 'app/register.html')


def user_login(request):
    #implement login
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print "LOGIN SUCCESS"
                return redirect('/sublet/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login.html')


@login_required
def user_logout(request):
    #implement logout
    logout(request)
    print "LOGOUT SUCCESS"
    return redirect('/sublet/')


def listings(request):
    listing_query = ListingOwned.objects
    shards = get_all_shards()
    listings_owned = []
    for shard in shards:
        set_db_for_sharding(listing_query, shard)
        listings_owned += listing_query.filter(is_booked=0)
        print('listings',listings_owned)

    print('listings',listings_owned)
    return render(request, 'app/listings.html', {'listings': listings_owned})


def apartments(request):
    apartment_query = ApartmentOwned.objects
    shards = get_all_shards()
    apartments_owned = []

    for shard in shards:
        print shard
        set_db_for_sharding(apartment_query, shard)
        print apartment_query.all().exclude(user_pk=2)
        apartments_owned += apartment_query.all().exclude(user_pk=2)

    # for shard in shards:
    #     set_db_for_sharding(apartment_query, shard)
    #     if apartments_owned == []:
    #         apartments_owned = apartment_query.all().exclude(user_pk=2)
    #         print('111apartments: ',apartments_owned)
    #     else:
    #         print('prev222apartments: ',apartments_owned)#merge querysets
    #         apartments_owned = list(chain(apartments_owned, apartment_query.all().exclude(user_pk=2)))
    #         print('222apartments: ',apartments_owned)#merge querysets
    
    print('apartments: ',apartments_owned)
    return render(request, 'app/apartments.html', {'apartments': apartments_owned})


def listing(request, shard_id, list_id):
    print(shard_id)
    listing_query = ListingOwned.objects
    set_user_for_sharding(listing_query, shard_id)
    listing = listing_query.get(pk=list_id)

    return render(request, 'app/listing.html', {'listing': listing})


def apartment(request, shard_id, apt_id):
    print(shard_id)
    apt_query = ApartmentOwned.objects
    set_user_for_sharding(apt_query, shard_id)
    apartment = apt_query.get(pk=apt_id)

    return render(request, 'app/apartment.html', {'apartment': apartment})

def bookings(request):
    booking_query = BookingPlaced.objects
    shards = get_all_shards()
    bookings_owned = []
    
    for shard in shards:
        set_db_for_sharding(booking_query, shard)
        bookings_owned +=  booking_query.all()

    print('bookings',bookings_owned)
   
    return render(request, 'app/bookings.html', {'bookings': bookings_owned})

def booking(request):
    return


@login_required
def profile(request):
    user_query = SubletUser.objects
    set_user_for_sharding(user_query, request.user.id)
    user = user_query.get(user_pk=request.user.id)

    #find all my apts
    apt_query = ApartmentOwned.objects
    set_user_for_sharding(apt_query, request.user.id)
    my_apartments = apt_query.filter(user=user)
    print ("my apts:" , my_apartments)
    #find all my current open listing
    listing_query = ListingOwned.objects
    set_user_for_sharding(listing_query, request.user.id)
    open_listings = listing_query.filter(user_pk=request.user.id, is_booked = 0)
    print  ("open_listings:" , open_listings)

    #find all my closed listing
    closed_listings = listing_query.filter(user_pk=request.user.id, is_booked = 1)
    print  ("closed_listings:" , closed_listings)

    #find all my bookings
    bookings_query = BookingPlaced.objects
    set_user_for_sharding(bookings_query, request.user.id)
    my_bookings = bookings_query.filter(user=user)
    print  ("my_bookings:" , my_bookings)

    return render(request, 'app/profile.html', {'s_user': user, 'apartments': my_apartments, 'open_listings': open_listings, 'closed_listings': closed_listings, 'bookings': my_bookings})


def processOffer(request):
    return


def addListing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        apartment_id = request.POST.get('apartment')

        user_query = ApartmentOwned.objects
        set_user_for_sharding(user_query, request.user.id)
        apartment = user_query.get(pk=apartment_id)

        new_listing = ListingOwned(user_pk=request.user.id, title=title, price=price, duration=duration, apartment=apartment)
        new_listing.save()
        return redirect('/sublet/listings/')
    else:
        user_query = SubletUser.objects
        set_user_for_sharding(user_query, request.user.id)
        user = user_query.get(user_pk=request.user.id)

        apt_query = ApartmentOwned.objects
        set_user_for_sharding(apt_query, request.user.id)
     

        apartments = apt_query.filter(user=user)
        json_apartments = []
        for apartment in apartments:
            json_apartments.append([apartment.get_address(), apartment.sqFt, apartment.year, apartment.min_from_subway])
        return render(request, 'app/addlisting.html', {'apartments': apartments, 'json_apartments': json_apartments})


def addApartment(request):
    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        
        user_query = SubletUser.objects
        set_user_for_sharding(user_query, request.user.id)
        user = user_query.get(user_pk=request.user.id)

       
        sqFt = float(request.POST.get('sqFt'))
        year = int(request.POST.get('year'))
        min_from_subway = int(request.POST.get('min'))

        apartment = ApartmentOwned(user_pk=request.user.id, street=street, city=city, state=state, zip=zip, user=user, sqFt=sqFt, year=year, min_from_subway=min_from_subway)
        apartment.save()
        return redirect('/sublet/apartments/')
    else:
        return render(request, 'app/addapartment.html')

def book(request):
    if request.method == 'POST':

        listing_query = ListingOwned.objects
        set_user_for_sharding(listing_query, request.POST.get('shard_id'))
        l = listing_query.get(pk=request.POST.get('list_id'))

        print l
        if not l.is_booked:
            a = l.apartment
            user_pk = request.user.id

            user_query = SubletUser.objects
            set_user_for_sharding(user_query, user_pk)
            s_user = user_query.get(user_pk=user_pk)
    
            apartment_wanted = ApartmentWanted(user_pk=user_pk, street=a.street, city=a.city, state=a.state, zip=a.zip, user=s_user, sqFt=a.sqFt, year=a.year, min_from_subway=a.min_from_subway)
            apartment_wanted.save()
            listing_wanted = ListingWanted(user_pk=user_pk, title=l.title, price=l.price, duration=l.duration, apartment=apartment_wanted)
            listing_wanted.save()
            booking_placed = BookingPlaced(user_pk=user_pk, duration=listing_wanted.duration, listing=listing_wanted, user=s_user)
            booking_placed.save()
            l.is_booked = True
            l.save()
            print s_user, s_user.user_pk
            print apartment_wanted, apartment_wanted.user_pk
            print listing_wanted, listing_wanted.user_pk
            print booking_placed, booking_placed.user_pk
            return JsonResponse({'success': 'success'})
        else:
            return  JsonResponse({'success': 'Listing already booked'})
            # return redirect('/sublet/bookings')
    else:
        return render(request, 'app/listings.html')


def estimate(request):
    #estimate = someFunc()
    sqft = request.POST.get('sqft')
    year = request.POST.get('year')
    min_from_subway = request.POST.get('min_from_subway')
    price = getEstimatedPrice(sqft, year,min_from_subway )
    print sqft, year, min_from_subway, price
    return JsonResponse({'success': "hello"})