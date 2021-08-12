from rest_framework import serializers
from .models import RoomChat

class RoomChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChat
        fields = ('id', 'code', 'host', 'skip_song_votes', 'created_at',)

class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomChat
        fields = ('skip_song_votes',)