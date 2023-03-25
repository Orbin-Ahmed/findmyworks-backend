from rest_framework import serializers
from quiz.models import SkillQuizQuestion


class SkillQuizSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = SkillQuizQuestion
        fields = [
            "id",
            "title",
            "a",
            "b",
            "c",
            "d",
        ]
