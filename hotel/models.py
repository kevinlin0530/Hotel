from django.db import models
from owner.models import Owner
from django.contrib import admin
# Create your models here.


class Hotel(models.Model):
    hotel_name = models.CharField(max_length = 30,unique=True)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,to_field='owner_name',related_name='hotel_name')
    def __str__(self):
        return self.hotel_name

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hotel._meta.fields] 
    search_fields = ('hotel_name','owner',)