from django.db import models

# Create your models here.
# django's ORM

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

