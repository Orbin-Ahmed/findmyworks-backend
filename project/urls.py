from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet, ProjectActivityAPIView, AllProjectAPIView, SponsorAPIViewSet

app_name = "project"

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('project-activities', ProjectActivityAPIView)
router.register('all-projects', AllProjectAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/sponsor/', SponsorAPIViewSet.as_view()),
]
