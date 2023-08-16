from django.shortcuts import render
from .serializer import RoomSerializer
from agent.models import Agent
from.models import Room
from hotel.models import Hotel
from management.permisson import   IsOwnerOrAgent
from rest_framework import viewsets , status
from rest_framework.permissions import IsAdminUser , AllowAny ,IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class RoomModel(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsOwnerOrAgent]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self,request):
        room_name = request.POST.get("room_name",'')
        queryset = Room.objects.filter(room_name=room_name)
        if queryset.exists():
            serializer = RoomSerializer(queryset,many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            result = {"status":"查無此房型"}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        
    def create(self,request):
        room_name = request.POST.get("room_name")
        hotel_name = request.POST.get("hotel")
        agent_name = request.POST.get("agent_name")

        try:
            hotel = Hotel.objects.get(hotel_name=hotel_name)
        except Hotel.DoesNotExist:
            result = {"status": "指定的飯店名稱不存在"}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        try:
            agent = Agent.objects.get(agent_name=agent_name, hotel=hotel)
        except Agent.DoesNotExist:
            result = {"status": "非指定的代理名稱"}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
            
        if agent.hotel != hotel:
            result = {"status": "無法更改此飯店的房型"}
            return Response(result, status=status.HTTP_403_FORBIDDEN)

        
        try:
            existing_room = Room.objects.get(room_name=room_name, hotel=hotel)
            if existing_room:
                result = {"status": "此房型已存在"}
                return Response(result, status=status.HTTP_208_ALREADY_REPORTED)
        except Room.DoesNotExist:
            pass

        data = {
            "room_name": room_name,
            "hotel": hotel
        }
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            result = {"status": "請輸入有效的房型資訊"}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)