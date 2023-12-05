from django.db import models
from django.utils import timezone
from django.conf import settings
import django.contrib.admin


class BaseDefaultFields(models.Model):
	class Meta:
		abstract = True

	created_at = models.DateTimeField(default=timezone.now, null=False)

class DefaultFields(BaseDefaultFields):
	class Meta:
		abstract = True

	updated_at = models.DateTimeField(auto_now=True)
	created_by = models.ForeignKey(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		db_index=False,
		related_name='+',
		related_query_name='+',
	)
	updated_by = models.ForeignKey(
		to=settings.AUTH_USER_MODEL,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		db_index=False,
		related_name='+',
		related_query_name='+',
	)
	# TODO: Handle created_by and updated_by in save method of this class


class ShallowDeleteModelQuerySet(models.QuerySet):
	def hard_delete(self):
		return super().delete()

	def delete(self):
		return self.update(
			deleted_at=timezone.now(),
		)

	def restore(self):
		return self.update(
			deleted_at=None,
		)


class ShallowDeleteModelAllManager(models.Manager):
	def get_queryset(self):
		return ShallowDeleteModelQuerySet(
			model=self.model,
			using=self._db,
		)


class ShallowDeleteModelManager(ShallowDeleteModelAllManager):
	def get_queryset(self):
		return super().get_queryset().filter(deleted_at__isnull=True)


class ShallowDeleteModel(DefaultFields):
	"""
	Brings Shallow Delete (Soft Delete) to Models. By inheriting this class,
	your models will have shallow delete mechanism.
	It means we usually don't delete objects on this model.
	Instead, we populate deleted_at field with current time.

	**Important: You should implement Manager Level Shallow Delete per subclass. (override objects)**
	To do so, make objects = X in which X is a Subclass of ShallowDeleteModelManager,
	and make all_objects = Y in which Y is a subclass of ShallowDeleteModelAllManager
	"""

	deleted_at = models.DateTimeField(null=True, blank=True, default=None)

	def hard_delete(self, using=None, keep_parents=False):
		return super().delete(using, keep_parents)

	def delete(self, using=None, keep_parents=False):
		# TODO: Handle objects referring to this user and have on_delete=CASCADE
		self.deleted_at = timezone.now()
		self.save()

	def restore(self):
		if not self.deleted_at:
			return
		self.deleted_at = None
		self.save()

	class Meta:
		abstract = True


class ShallowDeleteAdminModel(django.contrib.admin.ModelAdmin):
    def get_queryset(self, request):
        """
		Copied from parent class, changing used manager.
		There was no way to do it with overriding and calling super()
        """
        qs = self.model.all_objects.get_queryset()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs