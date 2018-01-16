from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.urls import reverse

# Create your views here.

from .forms import SignUpForm

def register(request):
	
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.institute = form.cleaned_data.get('institute')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect(reverse('hunt'))
		else:
			context = {
				'form' : form,
			}
			return render(request,'register.html', context)

	form = SignUpForm()
	context = {
		'form' : form,
	}

	return render(request,'register.html', context)


def leaderboard(request):
	queryset = User.objects.order_by('-profile__current_level','profile__current_level_time')
	context = {
		'queryset' : queryset,
	}
	return render(request, 'leaderboard.html', context)


def home(request):
	return render(request, 'home.html')

def rules(request):
	return render(request, 'rules.html')