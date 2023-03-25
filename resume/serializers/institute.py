from rest_framework import serializers

from resume.models import EducationInstitute, ProfessionalInstitute, Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["id", "name", "institute_type"]


class EducationInstituteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = EducationInstitute
        fields = [
            "id",
            "institute",
            "address",
            "start_date",
            "end_date",
            "currently_studying",
            "concentration",
            "major",
            "result",
            "extra_activities",
        ]


class EducationInstituteDetailsSerializer(serializers.ModelSerializer):
    institute = serializers.SerializerMethodField()

    @staticmethod
    def get_institute(instance):
        return InstituteSerializer(instance.institute).data
    class Meta:
        model = EducationInstitute
        fields = [
            "id",
            "institute",
            "address",
            "start_date",
            "end_date",
            "currently_studying",
            "concentration",
            "major",
            "result",
            "extra_activities",
        ]


class ProfessionalInstituteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = ProfessionalInstitute
        fields = [
            "id",
            "name",
            "designation",
            "city",
            "country",
            "start_date",
            "end_date",
            "currently_working",
            "responsibility",
        ]
