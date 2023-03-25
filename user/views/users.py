from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.filters import UserFilter
from user.models import User
from user.serializers import AllUsersSerializer


class AllUsersAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AllUsersSerializer
    queryset = User.objects.filter(is_superuser=False)
    filterset_class = UserFilter
    http_method_names = ['get']
