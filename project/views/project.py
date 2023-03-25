from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from project.filters import AllProjectFilter, ProjectFilter
from project.models import Project
from project.serializers import ProjectCreateSerializer, ProjectDetailSerializer, ProjectSponsorshipSerializer
from project.services import ProjectService, ProjectImageService


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]
    service_class = ProjectService()
    filterset_class = ProjectFilter
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_class(self):
        if self.action == 'create':
            return self.serializer_class
        elif self.action == 'update':
            return self.serializer_class
        else:
            return ProjectDetailSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data["user"] = request.user
        kwargs["request"] = request
        instance = self.service_class.create(validated_data, **kwargs)
        serializer = ProjectDetailSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data["user"] = request.user
        kwargs["request"] = request
        instance = self.get_object()
        instance = self.service_class.update(instance, validated_data, **kwargs)
        serializer = ProjectDetailSerializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.service_class.delete(instance, request.user, **kwargs)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["delete"], detail=True, url_path=r"delete-project-image/(?P<image_id>\d+)")
    def delete_project_image(self, request, pk, image_id):
        instance = self.get_object()
        project_image_service = ProjectImageService()
        data = {
            "id": int(image_id),
            "project": instance
        }
        project_image_service.delete(**data)
        return Response({"detail": "image delete successfully!"}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=True, url_path="add-project-sponsorship")
    def add_project_sponsorship(self, request, pk):
        instance = self.get_object()
        serializer = ProjectSponsorshipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        self.service_class.update_sponsorship(instance, validated_data)
        serializer = ProjectSponsorshipSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllProjectAPIView(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = AllProjectFilter
    http_method_names = ['get']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.serializer_class
        else:
            return self.serializer_class
