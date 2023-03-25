from rest_framework import serializers

from project.serializers import ProjectDetailSerializer
from project.services import ProjectService
from resume.serializers import EducationInstituteDetailsSerializer, ProfessionalInstituteSerializer
from resume.services import EducationInstituteService, ProfessionalInstituteService, RelatedInformationService
from user.models import User


class TalentSerializer(serializers.ModelSerializer):
    user_image = serializers.SerializerMethodField()

    def get_user_image(self, instance):
        related_information_service = RelatedInformationService()
        related_information_image = related_information_service.all(user=instance).first()
        return related_information_image.image if related_information_image else None

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "profession",
            "address",
            "bio",
            "email",
            "phone_number",
            "date_of_birth",
            "user_image"
        ]


class TalentDetailSerializer(serializers.ModelSerializer):
    eduction_institute = serializers.SerializerMethodField()
    professional_institute = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    user_image = serializers.SerializerMethodField()

    def get_eduction_institute(self, instance):
        education_institute_service = EducationInstituteService()
        education_institute = education_institute_service.all(user=instance)
        return EducationInstituteDetailsSerializer(education_institute, many=True).data

    def get_professional_institute(self, instance):
        professional_institute_service = ProfessionalInstituteService()
        professional_institute = professional_institute_service.all(user=instance)
        return ProfessionalInstituteSerializer(professional_institute, many=True).data

    def get_projects(self, instance):
        project_service = ProjectService()
        projects = project_service.all(user=instance)
        return ProjectDetailSerializer(projects, many=True).data

    def get_user_image(self, instance):
        related_information_service = RelatedInformationService()
        related_information_image = related_information_service.all(user=instance).first()
        return related_information_image.image if related_information_image else None

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "profession",
            "address",
            "bio",
            "email",
            "phone_number",
            "date_of_birth",
            "eduction_institute",
            "professional_institute",
            "projects",
            "user_image"
        ]
