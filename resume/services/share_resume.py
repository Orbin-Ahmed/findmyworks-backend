from rest_framework import status, serializers

from resume.serializers import AboutYourselfSerializer, EducationInstituteDetailsSerializer, \
    ProfessionalInstituteSerializer, AchievementSerializer, SkillSerializer, OtherRelatedInformationSerializer, \
    FinalizeRelatedInformationSerializer
from resume.services import EducationInstituteService, ProfessionalInstituteService, AchievementService, UserSkillService, \
    RelatedInformationService
from user.services import UserService


class ShareResumeService:
    user_service = UserService()
    educational_institute_service = EducationInstituteService()
    professional_institute_service = ProfessionalInstituteService()
    achievement_service = AchievementService()
    skill_service = UserSkillService()
    related_information_service = RelatedInformationService()

    def get_resume(self, user_id):
        status_code = status.HTTP_200_OK
        user = self.user_service.all(id=user_id).first()
        # user_skill = self.user_service.all(id=user_id).select_related('user_skill')
        if not user:
            raise serializers.ValidationError({"detail": "User not found!"})
        about_your_self = AboutYourselfSerializer(user).data
        educational_institutes = self.educational_institute_service.all(user=user)
        educational_institute_response = EducationInstituteDetailsSerializer(educational_institutes, many=True).data
        professional_institutes = self.professional_institute_service.all(user=user)
        professional_institute_response = ProfessionalInstituteSerializer(professional_institutes, many=True).data
        achievements = self.achievement_service.all(user=user)
        achievements_response = AchievementSerializer(achievements, many=True).data
        skills = self.skill_service.all(user=user)
        skills_response = SkillSerializer(skills, many=True).data
        related_information = self.related_information_service.all(user=user).first()
        other_related_information_response = OtherRelatedInformationSerializer(related_information).data
        finalize_related = FinalizeRelatedInformationSerializer(related_information).data
        resume = {
            "about_your_self": about_your_self,
            "educational_institute_response": educational_institute_response,
            "professional_institute_response": professional_institute_response,
            "achievements_response": achievements_response,
            "skills_response": skills_response,
            "other_related_information_response": other_related_information_response,
            "finalize_related": finalize_related,
        }
        return resume, status_code
