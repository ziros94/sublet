from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import ApartmentOwned, ApartmentWanted, ListingOwned, ListingWanted, BookingReceived, BookingPlaced, OfferPlaced, OfferReceived, SubletUser, User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from sharding import set_user_for_sharding, set_db_for_sharding, get_all_shards

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
    listings_owned = None
    for shard in shards:
        set_db_for_sharding(listing_query, shard)
        if listings_owned == None:
            listings_owned = listing_query.all()
        else:
            listings_owned = listings_owned | listing_query.all() #merge querysets

    #print('listings',listings_owned)
    return render(request, 'app/listings.html', {'listings': listings_owned})


def apartments(request):
    apartments_owned = ApartmentOwned.objects.all()
    return render(request, 'app/apartments.html', {'apartments': apartments_owned})


def listing(request, id=None):
    listing = get_object_or_404(ListingOwned, pk=id)
    return render(request, 'app/listing.html', {'listing': listing})


def bookings(request):
    bookings_placed = BookingPlaced.objects.all()
    return render(request, 'app/bookings.html', {'bookings': bookings_placed})

def booking(request):
    return


@login_required
def profile(request):
    user_query = SubletUser.objects
    set_user_for_sharding(user_query, request.user.id)
    sublet_user = user_query.get(user_pk=request.user.id)
    return render(request, 'app/profile.html', {'s_user': sublet_user})


def processOffer(request):
    return


def addListing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        apartment_id = request.POST.get('apartment')
        apartment = ApartmentOwned.objects.get(pk=apartment_id)
        new_listing = ListingOwned(user_pk=request.user.id, title=title, price=price, duration=duration, apartment=apartment)
        new_listing.save()
        return redirect('/sublet/listings')
    else:
        sublet_user = SubletUser.objects.get(user_pk=request.user.id)
        apartments = ApartmentOwned.objects.filter(user=sublet_user)
        return render(request, 'app/addlisting.html', {'apartments': apartments})


def addApartment(request):
    if request.method == 'POST':
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        user = SubletUser.objects.get(user_pk=request.user.id)
        sqFt = float(request.POST.get('sqFt'))
        year = int(request.POST.get('year'))
        doorman = bool(request.POST.get('doorman'))
        min_from_subway = int(request.POST.get('min'))
        apartment = ApartmentOwned(user_pk=request.user.id, street=street, city=city, state=state, zip=zip, user=user, sqFt=sqFt, year=year, has_doorman=doorman, min_from_subway=min_from_subway)
        apartment.save()
        return redirect('/sublet/apartments')
    else:
        return render(request, 'app/addapartment.html')


def book(request):
    if request.method == 'POST':
        l = ListingOwned.objects.get(user_pk=request.POST.get('shard_id'), id=request.POST.get('list_id'))
        print l
        if not l.is_booked:
            a = l.apartment
            u = a.user
            user_pk = request.user.id
            s_user = SubletUser(user_pk=request.user.id, username=u.username, first_name=u.first_name, last_name=u.last_name, email=u.email)
            s_user.save()
            apartment_wanted = ApartmentWanted(user_pk=user_pk, street=a.street, city=a.city, state=a.state, zip=a.zip, user=s_user, sqFt=a.sqFt, year=a.year, has_doorman=a.has_doorman, min_from_subway=a.min_from_subway)
            apartment_wanted.save()
            listing_wanted = ListingWanted(user_pk=user_pk, title=l.title, price=l.price, duration=l.duration, apartment=apartment_wanted)
            listing_wanted.save()
            booking_placed = BookingPlaced(user_pk=user_pk, duration=listing_wanted.duration, listing=listing_wanted, user=SubletUser.objects.get(user_pk=user_pk,username=request.user.username))
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