from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField() #Definging part of url or post
    date = models.DateField(auto_now_add=True)