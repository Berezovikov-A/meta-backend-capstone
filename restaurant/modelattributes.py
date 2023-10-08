from .models import Menu
from .serializers import MenuSerializer


class MenuItemAttr:
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
