from django.contrib import admin
from core.models.mixins import ShallowDeleteAdminModel

from core.models import (
    User,
    Project,
    TelegramBot,
    TelegramBotProjectAccess,
    UserProject,
)

@admin.register(User)
class UserAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'username',
        'is_superuser',
        'is_staff',
        'email',
        'first_name',
        'last_name',
    ]


@admin.register(Project)
class ProjectAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'name',
    ]


@admin.register(TelegramBot)
class TelegramBotAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'name',
        'username',
        'bot_id',
        'token',
    ]
