from rest_framework import serializers

from sender.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'receiver_id',
            'chat_id',
            'project_id',
            'sender_bot_id',
            'text',
        ]
        # TODO: Test if fields are given okay. definitely need more validations,
        # meaning we have to check if the _id is correct, and check for read_only, write_only attributes.


    def save(self, **kwargs):
        pass
        # TODO: Implement saving Message object here, getting data from kwargs

    def validate_project_id(self, data):
        pass
        # TODO: Implement

    def validate_sender_bot_id(self, data):
        # TODO: Implement
        pass
