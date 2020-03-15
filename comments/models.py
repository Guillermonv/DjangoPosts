from django.db import models

from posts.models import Post as Post
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, null=True, default=1, blank=True)
    name = models.CharField(max_length=20,blank=True, null=True)
    email = models.EmailField(max_length=20,blank=True, null=True)
    body = models.TextField(max_length=200,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    active = models.BooleanField(default=True,blank=True, null=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

