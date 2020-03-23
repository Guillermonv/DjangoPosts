# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):


   user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


   profile = models.ForeignKey('users.Profiles', on_delete=models.CASCADE,blank=True,null=True,default=0)
   title = models.CharField(max_length=100, blank=True, null=True)
   desc = models.CharField(max_length=1000, blank=True, null=True)

   photo = models.ImageField(upload_to='posts/photos',blank=True,null=True,default="no-photo")

   created = models.DateTimeField(auto_now_add=True)
   modified = models.DateTimeField(auto_now=True)


   def __str__(self):
        return '{} by {}'.format(self.title ,self.user)


