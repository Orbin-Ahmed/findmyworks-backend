from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from project.filters import ProjectActivityFilter
from project.models import ProjectActivity
from project.serializers import ProjectActivitySerializer
from project.services import ProjectActivityService


class ProjectActivityAPIView(viewsets.ModelViewSet):
    queryset = ProjectActivity.objects.all()
    serializer_class = ProjectActivitySerializer
    http_method_names = ['get', 'put', 'post']
    permission_classes = [IsAuthenticated]
    filterset_class = ProjectActivityFilter
    service_class = ProjectActivityService()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data["user"] = request.user
        kwargs["request"] = request
        instance = self.service_class.create(validated_data, **kwargs)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)