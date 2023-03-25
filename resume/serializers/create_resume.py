from rest_framework import serializers

from resume.serializers import (
    AboutYourselfSerializer,
    EducationInstituteSerializer,
    ProfessionalInstituteSerializer,
    AchievementSerializer,
    OtherRelatedInformationSerializer,
    FinalizeRelatedInformationSerializer,
    UserSkillCreateSerializer,
)


class CreateResumeSerializer(serializers.Serializer):
    about_yourself = AboutYourselfSerializer(required=False, allow_null=True)
    educational_institutes = serializers.ListField(child=EducationInstituteSerializer(required=True, allow_null=False))
    professional_institutes = serializers.ListField(
        child=ProfessionalInstituteSerializer(required=True, allow_null=False)
    )
    achievements = serializers.ListField(child=AchievementSerializer(required=True, allow_null=False))
    skills = serializers.ListField(child=UserSkillCreateSerializer(required=True, allow_null=False))
    other_related_information = OtherRelatedInformationSerializer(required=False, allow_null=True)
    finalize_related_information = FinalizeRelatedInformationSerializer(required=False, allow_null=True)
