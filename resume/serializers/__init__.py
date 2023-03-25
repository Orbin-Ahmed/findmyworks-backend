from resume.serializers.about_yourself import AboutYourselfSerializer
from resume.serializers.achievement import AchievementSerializer
from resume.serializers.hire import HireSerializers
from resume.serializers.institute import (
    EducationInstituteSerializer,
    ProfessionalInstituteSerializer,
    EducationInstituteDetailsSerializer,
    InstituteSerializer,
)
from resume.serializers.ranking import UniversityRankingSerializer, CollegeRankingSerializer, SchoolRankingSerializer
from resume.serializers.related_information import (
    OtherRelatedInformationSerializer,
    FinalizeRelatedInformationSerializer,
    RelatedInformationImageSerializer,
    RelatedInformationImageDetailSerializer,
)
from resume.serializers.skill import SkillSerializer, UserSkillCreateSerializer
