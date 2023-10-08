from rest_framework.serializers import *
from .models import Menu, Booking


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
