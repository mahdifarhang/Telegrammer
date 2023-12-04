from rest_framework import serializers

from sender.models import Message

class MessageSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True, required=False, source='get_status_display')
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
            'project',
            'sender_bot',
        ]
        read_only_fields = [
            'sent_at',
            'telegram_message_id',
        ]
        # TODO: Test if fields are given okay. definitely need more validations,
        # meaning we have to check if the _id is correct, and check for read_only, write_only attributes.


    def validate_project(self, data):
        return data
        # TODO: Implement. Check if the user is allowed to use this project

    def validate_sender_bot(self, data):
        # TODO: Implement. Check if the user is allowed to use this project
        return data