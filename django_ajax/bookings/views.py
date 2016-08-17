from rest_framework import viewsets

from django_ajax.bookings.models import Booking
from django_ajax.bookings.serializer import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
