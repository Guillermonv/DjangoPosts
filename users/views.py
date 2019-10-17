from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from users.forms import ProfileForm
from users.models import Profiles
from users.forms import SignupForm
from django.views.generic import TemplateView
from django.views.generic import  DetailView
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error':'invalid credential'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password != confirmpassword:
            return render(request,'users/signup.html',{'error': 'passwords dont match'})
        try:
           user = User.objects.create_user(username=username, password=password)
           return redirect('login')
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'user already exists'})
    return render(request, 'users/signup.html')
"""
def signup_view(request):
nuevo usando el forms Signup Form NO ANDA VER USER FORM.PY ver DEFs
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request= request,
                  template_name='users/signup.html',
                  context={'form':form})
"""

def update_profile(request):

    """Update a user's profile view."""

    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if not hasattr(user, 'profiles'):
                Profiles.objects.create(**{
                    'website': "add your website", 'bio': 'add your bio', 'picture': '', 'user': user
                })
            user.profiles.website = data['website']
            user.profiles.bio = data['bio']
            user.profiles.picture = data['picture']
            user.profiles.save()

            return redirect('users/update_profile.html')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': user,
            'user': request.user,
            'form': form
        }
    )


class UserDetailView(LoginRequiredMixin,DetailView):

    template_name = 'users/detail.html'
    slug_field = 'username'
   # parametro de urls.py <str>
    slug_url_kwarg = 'username'
    queryset = User.objects.all()

    content_object_name ='user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return  context

@login_required
def scores(request):
   # import pdb; pdb.set_trace()
    users = User.objects.all().order_by('-created')
    return render(request, os.path.join(BASE_DIR,'templates','users','score.html'), {'users': users})
