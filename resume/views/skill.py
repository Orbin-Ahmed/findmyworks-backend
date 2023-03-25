from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from resume.filters import SkillFilter
from resume.models import UserSkill
from resume.serializers import SkillSerializer, UserSkillCreateSerializer
from resume.views.resume_base_viewset import ResumeBaseViewSet
from resume.services import UserSkillService


class SkillViewSet(ResumeBaseViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = SkillSerializer
    service_class = UserSkillService()

    def create(self, request, *args, **kwargs):
        serializer = UserSkillCreateSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        self.service_class.update_or_create_instance(validated_data, request.user, **kwargs)
        instances = self.service_class.all(user=self.request.user)
        serializer = self.get_serializer(instances, many=True)
        return Response(serializer.data)
    

class AllSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]
    filterset_class = SkillFilter

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
