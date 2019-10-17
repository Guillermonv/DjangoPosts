
from django.urls import  path

from posts import views as postviews

urlpatterns = [
  path(route= '', view=postviews.renderize , name='feed'),
  path(route='posts/new',view=postviews.create_post,name='create_post'),
   path(route='posts/stats',view=postviews.stats,name='post_stats'),
  path(route='posts/hilarious',view=postviews.hilarious,name='post_hilarous'),
  path('comment/new', postviews.comment_new, name='comment_new'),
  #path(route='´post/comment<str:id>/',view=postviews.comment,name='comment'),
]