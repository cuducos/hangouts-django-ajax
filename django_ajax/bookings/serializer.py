from django.contrib.auth.models import User
from rest_framework import serializers

from django_ajax.bookings.models import Booking


class BookingSerializer(serializers.HyperlinkedModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=False,
        queryset=User.objects.all()
    )

    class Meta:
        model = Booking
        fields = ('user', 'event', 'date', 'created_on', 'authorized')
