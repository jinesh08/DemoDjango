import os
import random
import datetime

from datetime import timedelta
from django.utils import timezone

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
	user_photo = models.ImageField(upload_to = "user_images", blank = True, null = True)
	name = models.CharField(max_length = 100, blank = True, null = True)
	mobile = models.CharField(max_length = 12, blank = True, null = True)  #unique = True)
	new_mobile = models.CharField(max_length = 12, blank = True, null = True)
	email = models.CharField(max_length = 100, blank = True, null = True)

	is_deleted = models.BooleanField(default = False)
	created_at = models.DateTimeField(null = True, blank=True, default = datetime.datetime.now)

	def __str__(self):
	    return str(self.pk)

	class Meta:
	    verbose_name_plural = "User - unique"


class Credentials(models.Model):

	username = models.CharField(blank=True, max_length=100)
	password = models.CharField(blank=True, max_length=100)
	user = models.ForeignKey(User, blank=True, null = True)

	is_deleted = models.BooleanField(default = False)
	created_at = models.DateTimeField(null = True, blank=True, default = datetime.datetime.now)

	def __str__(self):
	    return str(self.pk)

	class Meta:
	    verbose_name_plural = "Credentails"


class UserToken(models.Model):

    token = models.CharField(blank=True, max_length=100)
    user = models.ForeignKey(User, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.token = "".join([random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for i in range(32)])
        super(UserToken, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.token

    class Meta:
        verbose_name_plural = "User Tokens"