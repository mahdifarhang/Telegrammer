from rest_framework.generics import CreateAPIView, RetrieveAPIView

from core.permissions import IsActiveAuthenticated
from sender.serializers import MessageSerializer
from sender.models import Message
from core.models import Project


class SendMessage(CreateAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        extra_content = {
            "status": Message.StatusChoices.SENDING,
        }
        serializer.save(**extra_content)
        # TODO: Start sending telegram message task


class GetMessage(RetrieveAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_project_ids = self.request.user.projects.all().values_list('id', flat=True)
        return Message.objects.filter(project_id__in=user_project_ids)


class CheckDoneTaskOrSentMessage():
    pass
    # TODO Implement
    # Important: Two things could happen, return the status of the message object, or check if the task for sending this message is being done or not, and check if the task is okay!
    