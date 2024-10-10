from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    profile_pic = models.CharField(max_length=1000, null=True)
    bio = models.CharField(max_length=255, null=True)

  

