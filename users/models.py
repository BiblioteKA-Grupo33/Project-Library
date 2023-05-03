from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    is_employe = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    
