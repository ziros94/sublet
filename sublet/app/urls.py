from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^listings/$', views.listings, name='listings'),
    url(r'^listing/(?P<id>[0-9]+)/$', views.listing, name='listing'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^booking/$', views.booking, name='booking'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^process/$', views.processOffer, name='processOffer'),
    url(r'^addlisting/$', views.addListing, name='addListing'),
]