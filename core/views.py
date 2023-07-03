from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from core.serializers import UserSerializer


class GetSelfUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
