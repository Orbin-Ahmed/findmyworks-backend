from core.services.base_model_service import BaseModelService
from quiz.models import SkillQuizResult


class SkillQuizResultService(BaseModelService):
    model_class = SkillQuizResult

    def update_or_create_quiz_result(self, validated_data):
        instance, _ = self.get_model_class().objects.update_or_create(
            skill=validated_data.get('skill'),
            user=validated_data.get('user'),
            defaults=validated_data
        )
