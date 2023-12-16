from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models.mixins import ShallowDeleteAdminModel

from core.models import (
    User,
    Project,
    TelegramBot,
    TelegramBotProjectAccess,
    UserProject,
)

class TelegramBotProjectAccessInline(admin.TabularInline):
    model = TelegramBotProjectAccess

class UserProjectInline(admin.TabularInline):
    model = UserProject

@admin.register(User)
class CustomUserAdmin(UserAdmin, ShallowDeleteAdminModel):
    list_display = [
        'id',
        'username',
        'is_superuser',
        'is_staff',
        'email',
        'first_name',
        'last_name',
    ]
    inlines = [UserProjectInline]


@admin.register(Project)
class ProjectAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'name',
    ]
    inlines = [UserProjectInline, TelegramBotProjectAccessInline]


@admin.register(TelegramBot)
class TelegramBotAdmin(ShallowDeleteAdminModel):
    list_display = [
        'id',
        'name',
        'username',
        'bot_id',
        'token',
    ]
    inlines = [TelegramBotProjectAccessInline, ]
