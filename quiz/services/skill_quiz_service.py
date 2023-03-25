from rest_framework import serializers

from core.services.base_model_service import BaseModelService
from quiz.models import SkillQuizQuestion
from quiz.services import SkillQuizResultService
from quiz.services.skill_service import SkillsService


class SkillQuizService(BaseModelService):
    model_class = SkillQuizQuestion
    skill_quiz_result_service = SkillQuizResultService()
    skill_service = SkillsService()

    @staticmethod
    def get_percentage(correct_ans, wrong_ans):
        percentage = (correct_ans * 100) / (correct_ans + wrong_ans)
        return percentage

    def get_random_question(self, skill, questions_no=10):
        # Todo: Refactor queryset
        questions = self.get_model_class().objects.filter(skill=skill).order_by('?')[:int(questions_no)]
        return questions

    def calculate_results(self, results, skill_id, user):
        correct_ans = 0
        wrong_ans = 0
        status = "Fail"
        skill = self.skill_service.all(id=skill_id).first()
        if not skill:
            raise serializers.ValidationError({"detail": "Skill not found!"})
        for result in results:
            correct_results = self.all(**result).first()
            if correct_results:
                correct_ans += 1
            else:
                wrong_ans += 1
        percentage = self.get_percentage(correct_ans, wrong_ans)
        if percentage > 70:
            status = "Pass"
        quiz_result = {
            "user": user,
            "skill": skill,
            "result_percent": percentage,
            "status": status
        }
        self.skill_quiz_result_service.update_or_create_quiz_result(quiz_result)
        result_status, percentage = status, percentage
        return result_status, percentage
