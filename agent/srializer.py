from rest_framework import serializers
from .models import Agent
#! 確認代理商管理的飯店與房型
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        # fields = '__all__'
        fields = [field.name for field in Agent._meta.fields] 
#! 確認代理商管理的飯店
class AgentHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Agent
        fields = ['agent_name','hotel'] 