from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models

from questions.models import Level
# Create your models here.

class Profile(models.Model):
	""" A Model Representing a User """

	user = models.OneToOneField(User, on_delete = models.CASCADE)
	institute = models.CharField(max_length=255, null=True)
	current_level = models.ForeignKey(Level, default = Level.DEFAULT_LEVEL)
	current_level_time = models.DateTimeField(default = timezone.now)
	is_banned = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)

	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
