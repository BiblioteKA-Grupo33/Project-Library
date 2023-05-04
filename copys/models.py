from django.db import models

class Copy(models.Model):
    
    book = models.ForeignKey(
        "books.Book",
        related_name="copy",
        on_delete=models.CASCADE
    )
