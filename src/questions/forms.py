from django import forms

# Import models

from .models import Level

class LevelForm(forms.ModelForm):
	class Meta:
		model = Level
		fields = [
			"answer"
		]