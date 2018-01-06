from django.shortcuts import render

# Create your views here.

from .forms import UserForm, UserModelForm

def register(request):
	form_user = UserForm()
	form_data = UserModelForm()

	context = {
		'form_user' : form_user,
		'form_data' : form_data,
	}

	return render(request,'register.html', context)