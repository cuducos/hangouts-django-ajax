from django.contrib import admin
from django_ajax.bookings.models import Booking


class BookingModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, BookingModelAdmin)
