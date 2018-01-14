from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Import Model
from .models import Profile

def email_validator(email):
	try:
		match = User.objects.get(email=email)
	except User.DoesNotExist:
		return email
	raise forms.ValidationError("Cannot use this email. It's already registered")
	return email

class SignUpForm(UserCreationForm):
	institute = forms.CharField(max_length=255)
	email = forms.EmailField(validators=[email_validator])
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		# Making name required
		self.fields['email'].required = True
		self.fields['first_name'].required = True
		self.fields['last_name'].required = True

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'institute' )
