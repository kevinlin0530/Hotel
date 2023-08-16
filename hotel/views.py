from django.shortcuts import render
from .serializer import HotelSerializer

from.models import Hotel

from management.permisson import   IsOwnerOrAgent
from rest_framework import viewsets , status
from rest_framework.permissions import IsAdminUser , AllowAny ,IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class HotelModel(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrAgent]
        return [permission() for permission in permission_classes]

    def list(self,request):
        hotel_name = request.POST.get("hotel_name",'')
        if not hotel_name.exists():
            result = {"status":"查無此飯店"}
            return Response(result,status=status.HTTP_404_NOT_FOUND)
        queryset = Hotel.objects.filter(hotel_name=hotel_name)
        if queryset.exists():
            serializer = HotelSerializer(queryset,many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            result = {"status":"查無此飯店"}
            return Response(result,status=status.HTTP_404_NOT_FOUND)