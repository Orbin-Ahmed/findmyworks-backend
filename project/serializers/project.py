import datetime

from rest_framework import serializers

from project.models import Project
from project.serializers.project_image import ProjectImageSerializer
from project.services import ProjectImageService
from resume.services import RelatedInformationService


class ProjectCreateSerializer(serializers.ModelSerializer):

    participants = serializers.ListField(required=False, allow_null=True)
    images = serializers.ListField(
        child=serializers.FileField(max_length=100000, allow_empty_file=False, use_url=False), required=False
    )

    class Meta:
        model = Project
        fields = ["id", "title", "project_link", "participants", "project_description", "images", "price", "category"]


class ProjectDetailSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    participants = serializers.SerializerMethodField()
    project_sponsorship = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()

    def get_image(self, instance):
        project_image_service = ProjectImageService()
        project_images = project_image_service.all(project=instance)
        images = ProjectImageSerializer(project_images, many=True)
        return images.data

    def get_participants(self, instance):
        related_information_service = RelatedInformationService()
        participants_list = []
        participants = instance.participants.all()
        for participant in participants:
            participants_image = related_information_service.all(
                user=participant
            ).first()
            participants_list.append(
                {
                    "email": participant.email,
                    "name": participant.full_name,
                    "image": participants_image.image if participants_image else None,
                }
            )
        return participants_list

    def get_project_sponsorship(self, instance):
        data = {}
        if instance.sponsors_due_date and instance.sponsors_due_date >= datetime.date.today():
            data = {
                "sponsors_due_date": instance.sponsors_due_date,
                "sponsor_description": instance.sponsor_description,
            }
        return data

    def get_created_by(self, instance):
        data = {
            "name": instance.created_by.full_name if instance.created_by else None,
            "email": instance.created_by.email if instance.created_by else None,
        }
        return data

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "category",
            "project_link",
            "participants",
            "project_description",
            "image",
            "price",
            "project_sponsorship",
            "category",
            "created_by"
        ]


class ProjectSponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "price",
            "sponsors_due_date",
            "sponsor_description",
        ]
