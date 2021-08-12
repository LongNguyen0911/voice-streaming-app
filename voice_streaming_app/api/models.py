from django.db import models
import string, random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if RoomChat.objects.filter(code=code).count() == 0:
            break
    
    return code

# Create your models here.
class RoomChat(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    host = models.CharField(max_length=50, unique=True)
    skip_song_votes = models.IntegerField(default=4, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code