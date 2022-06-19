from django.db import models
from django.conf import settings

# Create your models here.
class Title(models.Model):
    name = models.CharField(max_length=200)

class Text(models.Model):
    name = models.TextField


class Dates(models.Model):   
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

class Author(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )