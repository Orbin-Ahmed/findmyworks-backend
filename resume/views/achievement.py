from resume.models import Achievement
from resume.serializers import AchievementSerializer
from resume.views.resume_base_viewset import ResumeBaseViewSet
from resume.services import AchievementService


class AchievementViewSet(ResumeBaseViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    service_class = AchievementService()
