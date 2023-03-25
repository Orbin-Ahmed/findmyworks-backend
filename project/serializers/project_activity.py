from rest_framework import serializers

from project.models import ProjectActivity


class ProjectActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectActivity
        fields = ["project", "description",]
