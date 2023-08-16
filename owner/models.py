from django.db import models
from django.contrib import admin

# Create your models here.
class Owner(models.Model):
    owner_name = models.CharField(max_length = 30,unique=True)
    def __str__(self):
        return self.owner_name


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Owner._meta.fields] 
    search_fields = ('owner_name',)