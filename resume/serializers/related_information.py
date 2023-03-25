from rest_framework import serializers

from findmyworks import settings
from resume.models import RelatedInformation, RelatedInformationImage
from django.contrib.sites.shortcuts import get_current_site


class OtherRelatedInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedInformation
        fields = [
            "id",
            "other_skills",
        ]


class FinalizeRelatedInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedInformation
        fields = ["id", "image", "social_links", "publications"]


class RelatedInformationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedInformationImage
        fields = ["image"]


class RelatedInformationImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        file_url = instance.image
        return f"{settings.MEDIA_URL}{file_url}"

    class Meta:
        model = RelatedInformationImage
        fields = ["id", "image"]
