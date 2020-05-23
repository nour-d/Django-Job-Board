from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #  https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
    first_name = forms.CharField(label='Company Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Company Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
