from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserQueryset(models.QuerySet):
	def delete(self):
		return self.update(is_deleted=True)


class UserManager(models.Manager):
	def get_queryset(self):
		return UserQueryset(
			model=self.model,
			using=self._db
		).filter(is_deleted=False)


class User(AbstractUser):
	"""
	UserModel supports shallow delete. meaning we usually don't delete objects on this model.
	Instead, we set is_deleted field to True.
	In order not to have errors, objects is changed
	"""
	is_deleted = models.BooleanField(default=False, null=False)
	deleted_at = models.DateTimeField(null=True, blank=True, default=None)

	objects = UserManager()
	all_objects = models.Manager()

	def delete(self, using=None, keep_parents=False):
		# TODO: Handle objects referring to this user and have on_delete=CASCADE
		self.is_deleted = True
		self.deleted_at = timezone.now()
		self.save()

	def restore(self):
		if not self.is_deleted:
			return
		self.is_deleted = False
		self.deleted_at = None
		self.save()


	def represent(self):
		if self.last_name:
			if self.first_name:
				return f'{self.first_name} {self.last_name}'
			return self.last_name
		if self.email:
			return self.email
		return self.username

	def __str__(self):
		return self.represent()

	def __repr__(self):
		return self.represent()

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'
		default_manager_name = 'objects'
		base_manager_name = 'objects'
