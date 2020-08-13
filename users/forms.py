from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
            # 'password1',
            # 'password2',
        ]

class UserUpdate(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'last_name',
            'first_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    #profile = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [
            'genre',
            'experence',
            'wht',
            'langages',
            'avatar',
        ]

class EditProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    profile = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [
            'genre',
            'experence',
            'wht',
            'langages',
            'pays',
            'ville',
            'facebook',
            'twitter',
            'avatar',
            'bio'
        ]