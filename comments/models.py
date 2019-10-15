from django.db import models
#from posts.models import Post
from django.contrib.auth.models import User
# Create your models here.


class Comment(models.Model):
    """
    #id= models.AutoField(max_length=1000, blank=True)

    # post = models.ForeignKey(Post, related_name='',on_delete=models.CASCADE,default=0)
    """

    #comment = models.ForeignKey('posts.Post', related_name='posts_rel', to_field="comments", db_column="comments",
     #                           on_delete=models.CASCADE, null=True, default=1, blank=True)
    post = models.IntegerField(blank=True,null=True,unique=True,default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=0,null=True)

    #comment_in_post = models.CharField(max_length=1000, blank=True, null=True)
""""

    #post = models.ManyToManyField(Post)
    #post = models.ForeignKey(Post, on_delete=models.CASCADE)
    """


