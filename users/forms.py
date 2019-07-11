
from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=40)
    password = forms.CharField(max_length=70,widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=70 ,widget=forms.PasswordInput)
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget= forms.EmailInput
    )


    """" def clean_username(self):
        Username must be unique
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username en Uso')
        return username

    
    def clean_password(self):
        Verify password
        data = super().clean()
        password = data['password']
        confirmpassword = data['confirmpassword']
                                 confirmpassword
        if password != password_confirm:
            raise forms.ValidationError('Password do not match')
        return data
    """

class ProfileForm(forms.Form):

    website = forms.URLField(max_length=100, required=True)
    bio = forms.CharField(max_length=100, required=False)

    picture = forms.ImageField()