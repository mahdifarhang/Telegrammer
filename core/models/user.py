from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DefaultUserManager

from core.models.mixins import (
	ShallowDeleteModel,
	ShallowDeleteModelManager,
	ShallowDeleteModelAllManager,
)


class UserAllManager(ShallowDeleteModelAllManager, DefaultUserManager):
	pass


class UserManager(ShallowDeleteModelManager, DefaultUserManager):
	pass


class User(AbstractUser, ShallowDeleteModel):

	objects = UserManager()
	all_objects = UserAllManager()

	def represent(self):
		result = 'User '
		if self.last_name:
			if self.first_name:
				return result + f'{self.first_name} {self.last_name}'
			return result + self.last_name
		if self.email:
			return result + self.email
		return result + self.username

	def __str__(self):
		return self.represent()

	def __repr__(self):
		return self.represent()

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'
		default_manager_name = 'objects'
		base_manager_name = 'objects'
