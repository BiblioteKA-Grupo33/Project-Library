from django.db import models

# Create your models here.
import uuid

class Follow(models.Model):
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="followers_user"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="followers_books"
    )
