from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Level
from .forms import LevelForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
"""
@login_required
def hunt(request):
	cur_user = User.objects.get(id=request.user.id)
	if cur_user.profile.is_banned:
		# ban page
		return render(request,home.html)
	cur_level = cur_user.profile.current_level
	answer = LevelForm(request.POST or None)
	context = {
		'level' : cur_level,
		'form' : answer, 
	}
	"""


class Hunt(LoginRequiredMixin, View):
	""" The Game """
	login_url = '/login/'
	redirect_field_name = 'home.html'


	form_class = LevelForm


	def get(self, request, *args, **kwargs):
		cur_user = User.objects.get(id=request.user.id)
		if cur_user.profile.is_banned:
			return render(request,'home.html')

		cur_level = cur_user.profile.current_level
		form = self.form_class()
		context = {
			'level' : cur_level,
			'form' : form, 
		}
		return render(request,'level.html',context)


	def post(self,request, *args, **kwargs):
		cur_user = User.objects.get(id=request.user.id)
		form = self.form_class(request.POST)
		if form.is_valid():
			print(request.user.username)
			return render(request, 'home.html')
		return render(request,'home.html')
