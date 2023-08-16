from django.db import models
from hotel.models import Hotel
from django.contrib import admin
# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=30)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,to_field='hotel_name',related_name='room_name')
    def __str__(self):
        return self.room_name


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Room._meta.fields] 
    search_fields = ('room_name','hotel',)