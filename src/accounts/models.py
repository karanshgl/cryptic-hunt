from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

from questions.models import Level
# Create your models here.

class UserModel(models.Model):
	""" A Model Representing a User """

	user = models.OneToOneField(User, on_delete = models.CASCADE)
	institute = models.CharField(max_length=255)
	current_level = models.ForeignKey(Level, default = Level.DEFAULT_LEVEL)
	current_level_time = models.DateTimeField(default = timezone.now)
	is_banned = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)

	def __unicode__(self):
		return self.user.username