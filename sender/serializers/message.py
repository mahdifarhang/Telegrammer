from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from sender.models import Message

class MessageSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True, required=False, source='get_status_display')
    enable_notification = serializers.CharField(required=False)
    parse_mode = serializers.CharField(required=False)
    class Meta:
        model = Message
        fields = [
            'id',
            'text',
            'status',
            'sent_at',
            'receiver_id',
            'chat_id',
            'telegram_message_id',
            "parse_mode",
            "enable_notification",
            'project',
            'sender_bot',
            'error',
        ]
        read_only_fields = [
            'sent_at',
            'telegram_message_id',
            'error'
        ]

    def save(self, **kwargs):
        return super().save(**kwargs)
    
    def validate(self, attrs):
        result = super().validate(attrs)
        if not result.get('sender_bot') in result.get('project').telegram_bots.all():
            raise ValidationError(detail=f"Invalid pk '{result.get('sender_bot').id}' for sender_bot."
                                  " Object does not exist!")

        # Note: Could have returned 404 instead of the default which is 400,
        # but it seems a bit weird to return a 404 on a post.
        return result
    
    def validate_project(self, value):
        user = self.context.get('request').user
        if not value in user.projects.all():
            raise ValidationError(detail=f"Invalid pk '{value.id}' for project."
                                  " Object does not exist!")
        return value