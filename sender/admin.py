from django.contrib import admin
from core.models.mixins import ShallowDeleteAdminModel

from sender.models import Message


@admin.register(Message)
class MessageAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'text',
        'status',
        'sent_at',
        'receiver_id',
        'chat_id',
        'telegram_message_id',
        'project',
        'sender_bot',
    ]