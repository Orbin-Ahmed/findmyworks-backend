from rest_framework import serializers

from resume.services import RelatedInformationService
from user.models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, instance):
        related_information_service = RelatedInformationService()
        user_image = related_information_service.all(user=instance).first()
        return user_image.image if user_image else None

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "profession",
            "phone_number",
            "date_of_birth",
            "address",
            "email",
            "id",
            "image"
        ]
        read_only_fields = ["email", "id"]
