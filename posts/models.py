from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static

from django.urls import path
from django.conf import settings


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    profile = models.ForeignKey('users.Profiles', on_delete=models.CASCADE,null=True,default="some")
    title = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(upload_to='posts/photos')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} by {}'.format(self.title ,self.user)


static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)