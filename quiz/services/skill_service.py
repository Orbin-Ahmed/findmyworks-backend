from core.services.base_model_service import BaseModelService
from quiz.models import Skills


class SkillsService(BaseModelService):
    model_class = Skills
