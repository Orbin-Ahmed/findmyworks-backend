from core.services.base_model_service import BaseModelService
from quiz.services.skill_service import SkillsService
from resume.models import UserSkill


class UserSkillService(BaseModelService):
    model_class = UserSkill
    skills_service = SkillsService()

    def update_or_create_instance(self, validated_data_list, user, **kwargs):
        for validated_data in validated_data_list:
            validated_data["user"] = user
            skill = self.skills_service.get_or_create_instance(validated_data.pop("name").lower())
            validated_data["skill"] = skill
            instance, _ = self.get_model_class().objects.update_or_create(
                id=validated_data.get("id"),
                defaults=validated_data
            )

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        model_class = self.get_model_class()
        request = kwargs.get("request")
        user = self.core_service.get_user(request)
        validated_data["created_by"] = user
        validated_data["updated_by"] = user
        skill = self.skills_service.get_or_create_instance(validated_data.pop("name").lower())
        validated_data["skill"] = skill
        instance = model_class.objects.create(**validated_data)
        return instance
