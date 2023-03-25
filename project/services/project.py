from core.services.base_model_service import BaseModelService
from core.utils import send_general_email
from findmyworks import settings
from project.models.project import Project
from project.services.project_image import ProjectImageService
from resume.services import InstituteService
from user.services import UserService


class ProjectService(BaseModelService):
    model_class = Project
    institute_service = InstituteService()

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        images = validated_data.pop('images', [])
        participants = validated_data.pop('participants', [])
        model_class = self.get_model_class()
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        instance = model_class.objects.create(**validated_data)
        participant_list = []
        for participant in participants:
            user_service = UserService()
            participant_user = user_service.all(email=participant).first()
            if participant_user:
                participant_list.append(participant_user.id)
                self.send_project_participant_email(participant_user, instance)
        instance.participants.set(participant_list)
        self.institute_service.update_delete_project_ranking(user, is_added=True)
        image_service = ProjectImageService()
        for image in images:
            image_data = {
                "image": image,
                "project": instance
            }
            image_service.create(image_data, **kwargs)
        return instance

    def update(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        images = validated_data.pop('images', [])
        participants = validated_data.pop('participants', [])
        user = self.core_service.get_user(request)
        validated_data['updated_by'] = user
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        participant_list = []
        for participant in participants:
            user_service = UserService()
            participant_user = user_service.all(email=participant).first()
            if participant_user:
                participant_list.append(participant_user.id)
                self.send_project_participant_email(participant_user, instance)
        instance.participants.clear()
        instance.participants.set(participant_list)
        image_service = ProjectImageService()
        for image in images:
            image_data = {
                "image": image,
                "project": instance
            }
            image_service.create(image_data, **kwargs)
        return instance

    def delete(self, instance, user, **kwargs):
        self.institute_service.update_delete_project_ranking(user, is_added=False)
        return

    @staticmethod
    def update_sponsorship(instance, validated_data):
        instance.price = validated_data.get("price")
        instance.sponsors_due_date = validated_data.get("sponsors_due_date")
        instance.sponsor_description = validated_data.get("sponsor_description")
        instance.save()
        return instance

    @staticmethod
    def send_project_participant_email(participant_user, project):
        site_name = "findmywork.com"
        subject_template_name = "project_participant/project_participant.txt"
        html_email_template_name = "project_participant/project_participant.html"
        default_email = settings.FROM_EMAIL
        extra_email_context = None
        context = {
            "to_email": participant_user.email,
            "message": "You have been congratulated for participating in this project.",
            "site_name": site_name,
            "user_name": participant_user.full_name,
            "project_name": project.title,
            **(extra_email_context or {}),
        }
        send_general_email(
            subject_template_name,
            context,
            default_email,
            participant_user.email,
            html_email_template_name,
        )
