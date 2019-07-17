
from django.urls import path
from django.views.generic import TemplateView
from users import views as userview
urlpatterns=[

#esto seria users/...."""

    path('login', userview.login_view, name='login'),
    path('logout', userview.logout_view, name='logout'),
    path('signup', userview.signup_view, name='signup'),
    #path(route='<str:username>/', view=TemplateView.as_view(template_name='users/detail.html'), name='detail'),
    path(route='<str:username>/', view=userview.UserDetailView.as_view(), name='detail'),
    path('me/profile', userview.update_profile, name='update_profile'),



]