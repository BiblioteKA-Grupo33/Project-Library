from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    is_employe = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    
