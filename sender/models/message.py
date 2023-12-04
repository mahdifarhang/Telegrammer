from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.mixins import (
    ShallowDeleteModel,
    ShallowDeleteModelManager,
    ShallowDeleteModelAllManager,
)
from core.models import TelegramBot, Project


class MessageAllManager(ShallowDeleteModelAllManager):
    pass


class MessageManager(ShallowDeleteModelManager):
    pass


class Message(ShallowDeleteModel):
    class StatusChoices(models.IntegerChoices):
        SENDING = 11, _("Sending")
        SENT = 21, _("Sent")
        FAILED = 31, _("Failed")

    text = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=StatusChoices.choices,
        default=StatusChoices.SENDING,
        null=False,
        blank=False,
    )
    sent_at = models.DateTimeField(null=True, blank=True, default=None)
    receiver_id = models.CharField(
        max_length=64,
        null=False,
    )
    chat_id = models.CharField(
        max_length=64,
        null=False,
    )
    telegram_message_id = models.CharField(
        max_length=64,
        unique=True,
        null=True,
    )
    sender_bot = models.ForeignKey(
        to=TelegramBot,
        on_delete=models.PROTECT,
        related_name="messages",
        related_query_name="message",
        null=False,
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.PROTECT,
        related_name="messages",
        related_query_name="message",
    )
    """
    unsent_at, changed_at and other stuff can come later.
    """
    
    objects = MessageManager()
    all_objects = MessageAllManager()

    def representation(self):
        return f'Message {self.id}'

    def __str__(self):
        return self.representation()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        default_manager_name = 'objects'
        base_manager_name = 'objects'
