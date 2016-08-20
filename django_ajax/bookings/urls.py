from django.conf.urls import url

from django_ajax.bookings.views import list, list_date


urlpatterns = [
    url(r'^(?P<year>[\d]+)/(?P<month>[\d]+)/$', list_date, name='date'),
    url(r'$', list, name='list'),
]
