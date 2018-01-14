from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Import Model
from .models import Profile

class SignUpForm(UserCreationForm):
    institute = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'institute' )
