from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#https://stackoverflow.com/questions/36507909/model-has-no-foreignkey-to-auth-user


class Profiles(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=100, blank=True)
    bio = models.CharField(max_length=100, blank=True, null=True)
   # tittle = models.CharField(max_length=100, blank=True, null=True, default="TEST")
    phone_number = models.CharField(max_length= 20, blank=True)
    picture = models.ImageField(upload_to='users/picture',
                                blank=True,
                                null=True)

    create = models.DateTimeField(auto_now_add= True)

    modified = models.DateTimeField(auto_now = True)
   # def __str__ (self):
    #    return self.user.