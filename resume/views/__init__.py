from resume.views.about_yourself import AboutYourselfViewSet
from resume.views.achievement import AchievementViewSet
from resume.views.create_resume import CreateResumeAPIView
from resume.views.hire import HireAPIViewSet
from resume.views.institute import (
    EducationInstituteViewSet,
    ProfessionalInstituteViewSet,
    InstituteAPIView,
)
from resume.views.ranking import (
    UniversityRankingAPIView,
    CollegeRankingAPIView,
    SchoolRankingAPIView,
)
from resume.views.related_information import (
    OtherRelatedInformationViewSet,
    FinalizeRelatedInformationViewSet,
    RelatedInformationImageAPIView,
)
from resume.views.share_resume import ShareResume
from resume.views.skill import SkillViewSet, AllSkillViewSet
