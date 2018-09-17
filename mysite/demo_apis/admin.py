from django.contrib import admin
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from demo_apis.models import *

class CredentialsAdmin(SuperModelAdmin):
	model = Credentials
	list_display = ['pk', 'username', 'password', 'user' ,'is_deleted', 'created_at']

class UsersAdmin(SuperModelAdmin):
	model = User
	list_display = ['pk', 'name', 'mobile', 'email']


admin.site.register(Credentials, CredentialsAdmin)
admin.site.register(User, UsersAdmin)