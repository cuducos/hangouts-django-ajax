from calendar import Calendar
from datetime import date

from django.http import Http404
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from django_ajax.bookings.models import Booking
from django_ajax.bookings.serializer import BookingSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def list(request):
    selected_date = date.today()
    return list_date(request, selected_date.year, selected_date.month)


def list_date(request, year, month):

    try:
        selected_date = date(int(year), int(month), 1)
    except ValueError:
        raise Http404

    context = {
        'selected_date': selected_date,
        'calendar': tuple(_calendar(selected_date))
    }

    return render(request, 'bookings/bookings_list.html', context)


def _calendar(selected_date):
    year, month = selected_date.year, selected_date.month
    filters = {'date__year':  year, 'date__month': month}
    bookings = {b.date: b for b in Booking.objects.filter(**filters)}
    calendar = Calendar(firstweekday=6)
    for week in calendar.monthdatescalendar(year, month):
        yield [(day, bookings.get(day)) for day in week]
