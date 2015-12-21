from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^apartments/$', views.apartments, name='apartments'),
    url(r'^listings/$', views.listings, name='listings'),
    url(r'^listing/(?P<shard_id>[0-9]+)/(?P<list_id>[0-9]+)/$', views.listing, name='listing'),
    url(r'^bookings/$', views.bookings, name='bookings'),
    url(r'^booking/$', views.booking, name='booking'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^process/$', views.processOffer, name='processOffer'),
    url(r'^addlisting/$', views.addListing, name='addListing'),
    url(r'^addapartment/$', views.addApartment, name='addApartment'),
    url(r'^book/$', views.book, name='book'),
    url(r'^estimate/$', views.estimate, name='estimate'),
]