from django.urls import path
from .views import RoomChatView

urlpatterns = [
    path('rooms/', RoomChatView.as_view()),
]