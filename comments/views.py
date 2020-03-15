from django.shortcuts import render

# Create your views here.
from .models import Post, Comment
from .forms import  CommentForm
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def post_detail(request):
    if request.method == 'POST':
        pk = request.POST['pk']
    post = get_object_or_404(Post, pk=pk)
    # now you can filter the comments here
    comments = post.comment_set.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database

            new_comment.save()

    else:
        comment_form = CommentForm()
    return render(request,os.path.join(BASE_DIR,'templates','posts','feed_detail.html'),{'post': post,'comments': comments})
