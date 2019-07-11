
from django.contrib.auth.decorators import login_required

from django.shortcuts import render ,redirect
import os

from posts.forms import PostForm
# Create your views here.
from posts.models import Post

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@login_required
def renderize(request):
   # import pdb; pdb.set_trace()
    posts = Post.objects.all().order_by('-created')
    return render(request, os.path.join(BASE_DIR,'templates','posts','feed.html'), {'posts': posts})


from posts.models import User
@login_required()
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('VAAAAAALLIDDD')
            form.save()
            return redirect('feed')

    else:
        form = PostForm()
        print('INVALIDDDD')
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profiles': request.user.profiles
        }
    )
