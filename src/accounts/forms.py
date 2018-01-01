from django import forms
from django.contrib.auth.models import User

# Import Model
from .models import UserModel


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['__all__']


class UserModelForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ['institute']