from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete =models.CASCADE)
    date = models.DateField(default=timezone.now)
    image = models.ImageField(default = 'default.png', upload_to ='profile_pics')
    address = models.CharField(max_length=50, blank = True)
    city_town = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
