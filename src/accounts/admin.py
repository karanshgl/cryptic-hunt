from django.contrib import admin

# Register your models here.
from .models import UserModel

class UserAdminModel(admin.ModelAdmin):
	""" Admin Model """

	list_display = ["user", "current_level", "is_banned"]

	search_fields = ["user", "user.email"]

	class Meta:
		model = UserModel

admin.site.register(UserModel, UserAdminModel)