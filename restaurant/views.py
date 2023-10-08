from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from .modelattributes import MenuItemAttr, BookingAttr


def index(request: WSGIRequest):
    return render(request, 'index.html', {})


class MenuItemView(MenuItemAttr, ListCreateAPIView):
    pass


class SingleMenuItemView(MenuItemAttr, RetrieveUpdateDestroyAPIView):
    pass


class BookingViewSet(BookingAttr, ModelViewSet):
    pass
