from django.shortcuts import render
from rest_framework import generics
from .models import RoomChat
from .serializers import RoomChatSerializer

# Create your views here.
class RoomChatView(generics.ListAPIView):
    queryset = RoomChat.objects.all()
    serializer_class = RoomChatSerializer