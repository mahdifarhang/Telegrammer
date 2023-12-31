from rest_framework.generics import RetrieveAPIView, ListAPIView

from core.permissions import IsActiveAuthenticated
from core.models import TelegramBot
from core.serializers import UserSerializer, ProjectSerializer, TelegramBotSerializer


class GetSelfUserView(RetrieveAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class GetUserProjects(ListAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.request.user.projects.all().order_by('-created_at')


class GetUserTelegramBots(ListAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = TelegramBotSerializer

    def get_queryset(self):
        return TelegramBot.objects.filter(
            projects__users=self.request.user
        ).distinct('id').order_by('-id')
