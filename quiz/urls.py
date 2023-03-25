from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quiz.views import (
    SkillQuestionAPIView,
    SkillQuizSubmissionAPIView,
    SkillQuizResultAPIView,
    SkillQuizResultRankingAPIView,
    CertificatesAPIView
)

app_name = "quiz"

router = DefaultRouter()

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/questions/", SkillQuestionAPIView.as_view()),
    path("api/v1/results/", SkillQuizResultAPIView.as_view()),
    path(
        "api/v1/result-submissions/<int:skill_id>/",
        SkillQuizSubmissionAPIView.as_view(),
    ),
    path(
        "api/v1/ranking/",
        SkillQuizResultRankingAPIView.as_view(),
    ),
    path("api/v1/certificates/", CertificatesAPIView.as_view(),
         ),
]
