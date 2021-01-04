from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length = 40)
    phone = models.CharField(max_length =  10)
    image = models.ImageField(upload_to='profile_image', blank=True)
    balance = models.IntegerField(default=1000)
    def __str__(self):
        return self.name