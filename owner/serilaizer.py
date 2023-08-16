from rest_framework import serializers
from .models import Owner
from agent.models import Agent

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Owner
        # fields = '__all__'
        fields = [field.name for field in Owner._meta.fields] 
