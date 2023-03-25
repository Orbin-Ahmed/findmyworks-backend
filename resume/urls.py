from django.urls import path, include
from rest_framework.routers import DefaultRouter

from resume.views import (
    AboutYourselfViewSet,
    EducationInstituteViewSet,
    ProfessionalInstituteViewSet,
    AchievementViewSet,
    SkillViewSet,
    AllSkillViewSet,
    OtherRelatedInformationViewSet,
    FinalizeRelatedInformationViewSet,
    CreateResumeAPIView,
    InstituteAPIView,
    UniversityRankingAPIView,
    SchoolRankingAPIView,
    CollegeRankingAPIView,
    HireAPIViewSet,
    RelatedInformationImageAPIView,
    ShareResume,
)

app_name = "resume"


router = DefaultRouter()
router.register('about-yourself', AboutYourselfViewSet)
router.register('education-institutes', EducationInstituteViewSet)
router.register('professional-institutes', ProfessionalInstituteViewSet)
router.register('achievements', AchievementViewSet)
router.register('skills', SkillViewSet)
router.register('all-skills', AllSkillViewSet)
router.register('other-related-information', OtherRelatedInformationViewSet)
router.register('finalize-related-information', FinalizeRelatedInformationViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/create-resume/', CreateResumeAPIView.as_view()),
    path('api/v1/institutes/', InstituteAPIView.as_view()),
    path('api/v1/university-ranking/', UniversityRankingAPIView.as_view()),
    path('api/v1/college-ranking/', CollegeRankingAPIView.as_view()),
    path('api/v1/school-ranking/', SchoolRankingAPIView.as_view()),
    path('api/v1/hire/', HireAPIViewSet.as_view()),
    path('api/v1/related-information-image/', RelatedInformationImageAPIView.as_view()),
    path('api/v1/share-resume/<int:user_id>/', ShareResume.as_view()),
]
