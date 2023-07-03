from django.db import models

from core.models.mixins import (
	ShallowDeleteModel,
	BaseDefaultFields,
	ShallowDeleteModelManager,
	ShallowDeleteModelAllManager,
)


class TelegramBotAllManager(ShallowDeleteModelAllManager):
	pass


class TelegramBotManager(ShallowDeleteModelManager):
	pass


class TelegramBot(ShallowDeleteModel):
	name = models.CharField(max_length=50, null=False)
	token = models.CharField(max_length=70, unique=True)
	bot_id = models.CharField(max_length=60, unique=True)
	projects = models.ManyToManyField(
		to='core.Project',
		through='core.TelegramBotProjectAccess',
		blank=True,
		related_name='telegram_bots',
		related_query_name='telegram_bot',
	)

	objects = TelegramBotManager()
	all_objects = TelegramBotAllManager()

	def represent(self):
		return f'Telegram Bot {self.name}'

	def __str__(self):
		return self.represent()

	def __repr__(self):
		return self.represent()

	class Meta:
		verbose_name = 'Telegram Bot'
		verbose_name_plural = 'Telegram Bot'
		default_manager_name = 'objects'
		base_manager_name = 'objects'


class TelegramBotProjectAccess(BaseDefaultFields):
	project = models.ForeignKey(
		to='core.Project',
		on_delete=models.CASCADE,
		null=False,
		related_name='project_telegram_bots',
		related_query_name='project_telegram_bot',
	)
	telegram_bot = models.ForeignKey(
		to='core.TelegramBot',
		on_delete=models.CASCADE,
		null=False,
		related_name='telegram_bot_projects',
		related_query_name='telegram_bot_project',
	)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=['telegram_bot', 'project'],
				name='unique_together_telegram_bot_projects',
			),
		]
		verbose_name = 'Telegram Bot Project Access'
		verbose_name_plural = 'Telegram Bot Project Accesses'
