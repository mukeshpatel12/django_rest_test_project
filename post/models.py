from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User




class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=100)
    content = models.TextField()
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    created_at = models.DateTimeField('date published', auto_now_add=True)


    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return '"{title}" by {id}'.format(title=self.title,id=self.id)

