
from django.urls import  path

from posts import views as postviews
from comments import views as oommentviews

urlpatterns = [
  path(route= '', view=postviews.renderize , name='feed'),
  path(route='posts/new',view=postviews.create_post,name='create_post'),
  path(route='posts/stats',view=postviews.stats,name='post_stats'),
  path(route='posts/hilarious',view=postviews.hilarious,name='post_hilarous'),
  path(route='posts/detail', view=oommentviews.post_detail, name='post_detail'),
]