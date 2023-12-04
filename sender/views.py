from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response

from core.permissions import IsActiveAuthenticated
from sender.serializers import MessageSerializer


class SendMessage(GenericAPIView):
    permission_classes = [IsActiveAuthenticated]
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = self.send_message(serializer)
        return Response(data=response, status=status.HTTP_200_OK)

    def send_message(serializer):
        pass

