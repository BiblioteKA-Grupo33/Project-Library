from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField()
    realese_date = models.DateField()
    synopsis = models.TextField()
    author = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
