from rest_framework import serializers

from resume.models import Achievement


class AchievementSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Achievement
        fields = [
            "id",
            "title",
            "start_date",
            "end_date",
            "description",
            "currently_working",
            "links",
        ]
