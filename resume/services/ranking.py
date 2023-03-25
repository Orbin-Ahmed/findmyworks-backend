from django.db.models import F

from core.services.base_model_service import BaseModelService
from resume.models import Institute


class RankingService(BaseModelService):
    model_class = Institute

    def get_university_ranking(self):
        institutes = (
            self.get_model_class()
            .objects.filter(institute_type="university")
            .annotate(
                i_sum=F("total_members")
                + F("total_projects")
                + F("total_publications")
                + F("total_graduates")
                + F("total_job_placement")
            )
            .order_by("-i_sum")
        )
        return institutes

    def get_college_ranking(self):
        institutes = (
            self.get_model_class()
            .objects.filter(institute_type="college")
            .annotate(
                i_sum=F("total_members")
                + F("total_projects")
                + F("total_publications")
                + F("total_job_placement")
                + F("total_gpa")
            )
            .order_by("-i_sum")
        )
        return institutes

    def get_school_ranking(self):
        institutes = (
            self.get_model_class()
            .objects.filter(institute_type="school")
            .annotate(
                i_sum=F("total_members")
                + F("total_projects")
                + F("total_publications")
                + F("total_job_placement")
                + F("total_gpa")
            )
            .order_by("-i_sum")
        )
        return institutes
