from rest_framework import serializers

from project.models import ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = [
            "id",
            "image"
        ]
