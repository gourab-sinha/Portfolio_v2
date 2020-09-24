from django.contrib.auth.forms import UserCreationForm
from user.models import Profile, ProfileImage
from django.contrib.auth.forms import User
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', )


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ('image', )