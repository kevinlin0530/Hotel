from django.shortcuts import render

from .srializer import AgentSerializer,AgentHotelSerializer

from room.models import Room
from room.serializer import RoomSerializer

from.models import Agent

from management.permisson import   IsOwnerOrAgent
from rest_framework import viewsets , status
from rest_framework.permissions import IsAdminUser , AllowAny ,IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class AgentModel(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    # permission_classes = [IsOwnerOrAgent]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrAgent]
        return [permission() for permission in permission_classes]    

    def list(self,request):
        agent_name = request.POST.get('agent_name')
        hotel_name = request.POST.get('hotel')
        queryset = Agent.objects.filter(agent_name=agent_name)
        if not queryset.exists():
            result = {"status":"查無此人"}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        
        agent = queryset.first()
        if str(agent) != str(request.user):
            #! 代理人不是當前請求的用戶，返回未授權的回應
            return Response({"status": "未授權"}, status=status.HTTP_401_UNAUTHORIZED)
        
        #! 如果有飯店和代理人，回傳所管理的飯店和房型
        if hotel_name and agent_name:
            rooms = Room.objects.filter(hotel=hotel_name)
            serializer = RoomSerializer(rooms,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        #! 只有代理，回傳代理的所有飯店
        elif agent_name:
            serializer = AgentHotelSerializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)