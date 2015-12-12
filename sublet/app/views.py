from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import  Apartment, Listing, Booking, User, OfferPlaced, OfferReceived
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'app/home.html')


def user_login(request):
    #implement login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
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
    all_listings = Listing.objects.all()
    return render(request, 'app/listings.html', {'listings': all_listings})


def listing(request, id=None):
    listing = get_object_or_404(Listing, pk=id)
    return render(request, 'app/listing.html', {'listing': listing})


def bookings(request):
    return

def booking(request):
    return


@login_required
def profile(request):
    return render(request, 'app/profile.html')

def processOffer(request):
    return