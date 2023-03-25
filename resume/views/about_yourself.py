from rest_framework import status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from resume.serializers import AboutYourselfSerializer
from user.models import User
from user.services import UserService


class AboutYourselfViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AboutYourselfSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    user_service = UserService()

    def list(self, request, *args, **kwargs):
        user = self.queryset.filter(id=request.user.id).first()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        self.user_service.update(user, validated_data=validated_data, **kwargs)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
