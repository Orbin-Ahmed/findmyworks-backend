from rest_framework import serializers

from user.models import User


class AboutYourselfSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "profession",
            "phone_number",
            "date_of_birth",
            "address",
            "bio",
            "email"
        ]
        read_only_fields = ["email"]
