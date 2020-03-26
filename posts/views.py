
from django.contrib.auth.decorators import login_required

from django.shortcuts import render ,redirect
import os
from comments.forms import CommentForm
from users.forms import ProfileForm
from posts.forms import PostForm
# Create your views here.
from posts.models import Post
from comments.models import Comment
#from comment.models import Comment
from django.core.exceptions import PermissionDenied

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@login_required
def renderize(request):
   # import pdb; pdb.set_trace()
    posts = Post.objects.all().order_by('-created')
    comments = Comment.objects.all().order_by('-created')
    return render(request, os.path.join(BASE_DIR,'templates','posts','feed.html'), {'posts': posts, 'comments':comments})


from posts.models import User
#@login_required()
def create_post(request):
    
   # for key, value in request.POST.items():
    #    if(key == 'user'):            
     #       if(str(value) not in ['4','2','1']):
      #          raise PermissionDenied()
        


    """Create new post view."""            
  #  if(request.POST['user'] != 0):
   #   raise Exception('general exceptions not caught by specific handling')
    form = PostForm(request.POST, request.FILES)
    
    if form.is_valid():
        form.save()
        return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
           'profiles': request.user.profiles
        })

from django.core.mail import send_mail
#No usar
def comment_new(request):
    if request.method == 'POST':
        id = request.POST['user_id']
        #subject = request.POST['title']
        user = request.POST['username']
       # last_name = request.POST['last_name']

        #lastname = request.POST['lastname']
        print('ITEMS')
        for key, value in request.POST.items():
            print(str(key) + "--")
            print(str(value))
        form = CommentForm(request.POST, request.FILES)
   #     print formset.errors

        if form.is_valid():
            form.save()

       # send_mail("[ENGLISH] " + subject,user +" "+ last_name + " said  "+ message + " on http://english.darwoft.com:8000", 'guillermo.varelli@gmail.com',
       #     ['guillermo.varelli@darwoft.com'], fail_silently=False)

    posts = Post.objects.all().order_by('-created')
    return render(request, os.path.join(BASE_DIR,'templates','posts','feed.html'), {'posts': posts})

    
"""
para hacer trend de mensajes 
from django.shortcuts import get_object_or_404


def comment_new(request, pk):
    Update a user's profile view.
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

comment.post = post
            comment.save()
            return redirect('feed')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
"""


def stats(request):
   return render(request,"stats.html")

def hilarious(request):
   return render(request,"hilarious.html")
