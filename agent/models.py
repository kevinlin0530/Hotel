from django.db import models
from owner.models import Owner
from hotel.models import Hotel
from django.contrib import admin
# Create your models here.


class Agent(models.Model):
    agent_name = models.CharField(max_length = 30)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,to_field='owner_name',related_name='agents', null=True, blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,to_field='hotel_name',related_name='agents', null=True, blank=True)
    def __str__(self):
        return self.agent_name
    
@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Agent._meta.fields] 
    search_fields = ('agent_name','owner','hotel')