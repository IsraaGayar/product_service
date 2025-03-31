from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import URLValidator

class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True, validators=[URLValidator()])


    def __str__(self):
        return f"{self.user.username}'s Profile"