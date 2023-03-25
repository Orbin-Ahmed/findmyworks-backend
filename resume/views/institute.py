from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from resume.filters import InstituteFilter
from resume.models import EducationInstitute, ProfessionalInstitute, Institute
from resume.serializers import (
    EducationInstituteSerializer,
    ProfessionalInstituteSerializer,
    EducationInstituteDetailsSerializer,
    InstituteSerializer,
)
from resume.services import EducationInstituteService
from resume.services.institute import ProfessionalInstituteService, InstituteService
from resume.views.resume_base_viewset import ResumeBaseViewSet


class InstituteAPIView(ListAPIView):
    queryset = Institute.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    service_class = InstituteService()
    serializer_class = InstituteSerializer
    filterset_class = InstituteFilter


class EducationInstituteViewSet(ResumeBaseViewSet):
    queryset = EducationInstitute.objects.all()
    serializer_class = EducationInstituteSerializer
    detail_serializer_class = EducationInstituteDetailsSerializer
    service_class = EducationInstituteService()
    institute_service = InstituteService()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.detail_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.detail_serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        kwargs["request"] = request
        self.service_class.update_or_create_instance(validated_data, request.user, **kwargs)
        instances = self.service_class.all(user=self.request.user)
        serializer = self.detail_serializer_class(instances, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.institute_service.remove_ranking_values(instance)
        if instance.result == 5.00:
            self.institute_service.update_or_delete_gpa(instance, is_added=False)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfessionalInstituteViewSet(ResumeBaseViewSet):
    queryset = ProfessionalInstitute.objects.all()
    serializer_class = ProfessionalInstituteSerializer
    permission_classes = [IsAuthenticated]
    service_class = ProfessionalInstituteService()
    institute_service = InstituteService()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.institute_service.update_or_delete_job_placement(instance, is_added=False)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
