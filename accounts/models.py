from django.db import models
from django.contrib.auth.models import User




class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(default='https://i.pinimg.com/236x/16/3b/e0/163be007c96fbd738da26adf15d9fa5f--profiles-avatar.jpg')

    def __str__(self):
        return f'{self.user}'