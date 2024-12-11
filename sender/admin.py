from django.contrib import admin
from core.models.mixins import ShallowDeleteAdminModel

from sender.models import Message


@admin.register(Message)
class MessageAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'status',
        'enable_notification',
        'parse_mode',
        'chat_id',
        'project',
        'telegram_message_id',
        'sender_bot',
    ]
