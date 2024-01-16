from django.db import models
from BlogApp.models import Post
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    publishedDate = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
