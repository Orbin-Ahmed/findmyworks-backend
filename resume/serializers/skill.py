from rest_framework import serializers

from resume.models import UserSkill
from quiz.models import SkillQuizResult, SkillQuizQuestion


class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.SerializerMethodField()
    attend_quiz = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_name(self, instance):
        return instance.skill.name

    def get_question(self, instance):
        if instance.skill:
            x = instance.skill
            if SkillQuizQuestion.objects.filter(skill=x):
                return True
            else:
                return False
        else:
            return None

    def get_attend_quiz(self, instance):
        if instance.skill:
            x = instance.user
            y = instance.skill
            if SkillQuizResult.objects.filter(user=x, skill=y):
                return True
            else:
                return False
        else:
            return False

    def get_status(self, instance):
        if instance.skill:
            x = instance.user
            y = instance.skill
            if SkillQuizResult.objects.filter(user=x, skill=y):
                y = SkillQuizResult.objects.get(user=x, skill=y)
                return y.status
        else:
            return None

    def get_updated_at(self, instance):
        if instance.skill:
            x = instance.user
            y = instance.skill
            if SkillQuizResult.objects.filter(user=x, skill=y):
                y = SkillQuizResult.objects.get(user=x, skill=y)
                return y.updated_at
        else:
            return None
    class Meta:
        model = UserSkill
        fields = [
            "id",
            "name",
            "skill",
            "attend_quiz",
            "status",
            "updated_at",
            "question"
        ]


class UserSkillCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()

    class Meta:
        model = UserSkill
        fields = [
            "id",
            "name",
        ]
