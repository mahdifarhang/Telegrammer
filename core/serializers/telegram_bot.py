from rest_framework import serializers

from core.models import TelegramBot


class TelegramBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramBot
        fields = [
            'name',
            'token',
            'bot_id',
            'username',
            'created_at',
        ]