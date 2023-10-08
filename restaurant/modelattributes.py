from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


class MenuItemAttr:
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingAttr:
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
