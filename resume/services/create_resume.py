import datetime
import logging

from rest_framework import status
from resume.services import (
    EducationInstituteService,
    AchievementService,
    UserSkillService,
    ProfessionalInstituteService,
    RelatedInformationService,
)
from user.services import UserService

logger = logging.getLogger(__name__)


class CreateResumeService:
    user_service = UserService()
    educational_institute_service = EducationInstituteService()
    professional_institute_service = ProfessionalInstituteService()
    achievement_service = AchievementService()
    skill_service = UserSkillService()
    related_information_service = RelatedInformationService()

    def create(self, user, validated_data, **kwargs):
        try:
            about_yourself = validated_data.get("about_yourself", {})
            educational_institutes = validated_data.get("educational_institutes", {})
            professional_institutes = validated_data.get("professional_institutes", {})
            achievements = validated_data.get("achievements", {})
            skills = validated_data.get("skills", {})
            other_related_information = validated_data.get("other_related_information", {})
            finalize_related_information = validated_data.get("finalize_related_information", {})

            about_yourself["user"] = user if about_yourself else None
            other_related_information["user"] = user if other_related_information else None
            finalize_related_information["user"] = user if finalize_related_information else None

            self.user_service.update(user, validated_data=about_yourself, **kwargs)
            for institute in educational_institutes:
                institute["user"] = user
                self.educational_institute_service.create(validated_data=institute, **kwargs)
            for institutes in professional_institutes:
                institutes["user"] = user
                self.professional_institute_service.create(validated_data=institutes, **kwargs)
            for achievement in achievements:
                achievement["user"] = user
                self.achievement_service.create(validated_data=achievement, **kwargs)
            for skill in skills:
                skill["user"] = user
                self.skill_service.create(validated_data=skill, **kwargs)
            related_information_instance = self.related_information_service.all(user=user).first()
            self.related_information_service.update(related_information_instance, other_related_information, **kwargs)
            self.related_information_service.update(
                related_information_instance, finalize_related_information, **kwargs
            )
            message = "resume has been created!"
            resume_status = status.HTTP_201_CREATED
            return message, resume_status
        except Exception as e:
            message = "resume create failed!"
            resume_status = status.HTTP_400_BAD_REQUEST
            logger.error(f"{e}. Create resume service error! Time: {datetime.datetime.now()}")
            return message, resume_status
