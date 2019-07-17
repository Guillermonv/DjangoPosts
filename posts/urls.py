
from django.urls import  path

from posts import views as postviews

urlpatterns = [
  path(route= '', view=postviews.renderize , name='feed'),
  path(route='posts/new',view=postviews.create_post,name='create_post'),

]