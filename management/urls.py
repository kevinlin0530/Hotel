"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from owner.views import OwnerModel
from agent.views import AgentModel
from hotel.views import HotelModel
from room.views import RoomModel

owner_router = DefaultRouter()
owner_router.register(r'owner',OwnerModel)

agent_router = DefaultRouter()
agent_router.register(r'agent',AgentModel)

hotel_router = DefaultRouter()
hotel_router.register(r'hotel',HotelModel)

room_router = DefaultRouter()
room_router.register(r'room',RoomModel)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_owner/',include(owner_router.urls)),
    path("api_agent/",include(agent_router.urls)),
    path("api_hotel/",include(hotel_router.urls)),
    path("api_room/",include(room_router.urls)),
]
