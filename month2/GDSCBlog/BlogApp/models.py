from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField()
    Tags = models.TextField()