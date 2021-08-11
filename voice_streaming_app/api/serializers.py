from rest_framework import serializers
from .models import RoomChat

class RoomChatSerializer(serializers.Serializer):
    class Meta:
        model = RoomChat
        fields = ('__all__')