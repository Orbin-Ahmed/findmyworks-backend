from core.services.base_model_service import BaseModelService
from resume.models import Achievement


class AchievementService(BaseModelService):
    model_class = Achievement
