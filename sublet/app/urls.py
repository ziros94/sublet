from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^listings/$', views.listings, name='listings'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^bookings/$', views.bookings, name='listings'),
    url(r'^booking/$', views.booking, name='listing'),
    url(r'^profile/$', views.profile, name='profile'),
]