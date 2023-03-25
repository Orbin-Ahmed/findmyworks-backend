from rest_framework import serializers

from quiz.models import SkillQuizResult
from user.serializers import user_detail_serializer


class SkillQuizSubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    correct_ans = serializers.CharField()


class SkillQuizResultSerializer(serializers.ModelSerializer):
    user = user_detail_serializer.UserDetailsSerializer()
    class Meta:
        model = SkillQuizResult
        fields = ["skill", "result_percent", "updated_at", "status", "user"]


class CertificateSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    skill_name = serializers.SerializerMethodField()

    def get_skill_name(self, instance):
        return instance.skill.name

    def get_user_name(self, instance):
        return instance.user.full_name

    class Meta:
        model = SkillQuizResult
        fields = ["skill_name", "result_percent", "updated_at", "user_name"]
