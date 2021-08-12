from django.urls import path
from .views import RoomChatView, CreateRoomView

urlpatterns = [
    path('rooms/', RoomChatView.as_view()),
    path('create-room/', CreateRoomView.as_view()),
]