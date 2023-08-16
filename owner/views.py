from django.shortcuts import render
from .models import Owner
from agent.models import Agent
from .serilaizer import OwnerSerializer

from rest_framework import viewsets , status
from rest_framework.permissions import IsAdminUser , AllowAny ,IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class OwnerModel(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def list(self, request):
        owner_name = request.POST.get('owner_name')
        queryset = Owner.objects.filter(owner_name=owner_name)
        if not queryset.exists():
            resulte = {"status":"查無此人"}
            return Response(resulte , status=status.HTTP_200_OK)
        serializer =OwnerSerializer(queryset,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)