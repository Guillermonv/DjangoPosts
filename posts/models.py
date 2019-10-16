from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment

from django.urls import path
from django.conf import settings


class Post(models.Model):

    comments = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    #comment = models.ForeignKey('comments.comment',related_name='posts_rel', to_field="post", db_column="post",on_delete=models.CASCADE, null=True, default=1,blank=True)

    profile = models.ForeignKey('users.Profiles', on_delete=models.CASCADE,null=True,default=1,blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    desc = models.CharField(max_length=1000, blank=True, null=True)
   
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} by {}'.format(self.title ,self.user)


