from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Level
from .forms import LevelForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect



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
		cur_level = cur_user.profile.current_level
		form = self.form_class(request.POST)
		if form.is_valid():
			print(request.user.username)
			ans = form.cleaned_data.get('answer')
			if ans == cur_level.answer:
				l=cur_user.profile.current_level.level_id
				cur_user.profile.current_level = Level.objects.get(level_id=l+1)
				cur_user.profile.save()
			return redirect('/hunt/')
		return redirect('/hunt/')
