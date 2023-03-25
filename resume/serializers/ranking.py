from rest_framework import serializers

from resume.models import Institute


class UniversityRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
            "institute_type",
            "total_members",
            "total_projects",
            "total_publications",
            "total_job_placement",
            "total_graduates",
        ]


class CollegeRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
            "institute_type",
            "total_members",
            "total_projects",
            "total_publications",
            "total_job_placement",
            "total_gpa",
        ]


class SchoolRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = [
            "id",
            "name",
            "institute_type",
            "total_members",
            "total_projects",
            "total_publications",
            "total_job_placement",
            "total_gpa",
        ]
