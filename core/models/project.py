from django.db import models

from core.models.mixins import (
	ShallowDeleteModel,
	BaseDefaultFields,
	ShallowDeleteModelManager,
	ShallowDeleteModelAllManager,
)


class ProjectAllManager(ShallowDeleteModelAllManager):
	pass


class ProjectManager(ShallowDeleteModelManager):
	pass


class Project(ShallowDeleteModel):
	name = models.CharField(max_length=30, null=False)
	users = models.ManyToManyField(
		to='core.User',
		through='core.UserProject',
		blank=True,
		related_name='projects',
		related_query_name='project',
	)

	objects = ProjectManager()
	all_objects = ProjectAllManager()

	def represent(self):
		return f'Project {self.name}'

	def __str__(self):
		return self.represent()

	def __repr__(self):
		return self.represent()

	class Meta:
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'
		default_manager_name = 'objects'
		base_manager_name = 'objects'


class UserProject(BaseDefaultFields):
	user = models.ForeignKey(
		to='core.User',
		on_delete=models.CASCADE,
		null=False,
		related_name='user_projects',
		related_query_name='user_project',
	)
	project = models.ForeignKey(
		to='core.Project',
		on_delete=models.CASCADE,
		null=False,
		related_name='project_users',
		related_query_name='project_user',
	)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=['user', 'project'],
				name='unique_together_user_projects',
			),
		]
		verbose_name = 'User Project'
		verbose_name_plural = 'User Projects'
