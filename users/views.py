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

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error':'invalid credential'})
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


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

            return redirect('update_profile')

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


