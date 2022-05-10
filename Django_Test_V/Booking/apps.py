from django.apps import AppConfig
from django.contrib import admin
from .models import Room, RoomCat, Booking

admin.site.register(Room),
admin.site.register(RoomCat),
admin.site.register(Booking)
