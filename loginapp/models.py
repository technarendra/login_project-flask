from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    User = models.OneToOneField(User)
    #add some more field
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pic")

    def __str__(self):
        return self.user.username


