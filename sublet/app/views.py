from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import  Apartment, Listing, Booking, User, OfferPlaced, OfferReceived
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'app/index.html', {})


def user_login(request):
    #implement login
    return


def user_logout(request):
    #implement logout
    return

def listings(request):
    return

def listing(request):
    return

def bookings(request):
    return

def booking(request):
    return

def profile(request):
    return

