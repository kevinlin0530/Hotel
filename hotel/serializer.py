from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        # fields = '__all__'
        fields = [field.name for field in Hotel._meta.fields] 
