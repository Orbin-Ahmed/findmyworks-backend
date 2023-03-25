from allauth.account.models import EmailAddress
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from user.filters import TalentFilter
from user.models import User
from user.serializers import TalentSerializer, TalentDetailSerializer


class TalentAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TalentSerializer
    queryset = User.objects.all()
    filterset_class = TalentFilter
    http_method_names = ['get']

    def get_queryset(self):
        verify_email = EmailAddress.objects.filter(verified=True).values_list("email", flat=True)
        queryset = self.queryset.filter(is_superuser=False, email__in=verify_email)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TalentDetailSerializer
        else:
            return self.serializer_class
