from django.shortcuts import render
from rest_framework import generics, serializers, status
from .models import RoomChat
from .serializers import RoomChatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateRoomSerializer

# Create your views here.
class RoomChatView(generics.ListAPIView):
    queryset = RoomChat.objects.all()
    serializer_class = RoomChatSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            votes = serializer.data.get('skip_song_votes')
            host = self.request.session.session_key
            queryset = RoomChat.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.skip_song_votes = votes
                room.save(update_fields=['skip_song_votes'])
                return Response(RoomChatSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = RoomChat(host=host, skip_song_votes=votes)
                room.save()
                return Response(RoomChatSerializer(room).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)