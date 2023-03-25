from django.contrib import admin

from resume.models import (
    Achievement,
    ProfessionalInstitute,
    EducationInstitute,
    RelatedInformation,
    Institute,
    UserSkill,
)


@admin.register(Achievement)
class AchievementModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user"]
    search_fields = ["id", "title", "user__email"]


@admin.register(ProfessionalInstitute)
class ProfessionalInstituteModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "user"]
    search_fields = ["id", "name", "user__email"]


@admin.register(Institute)
class InstituteModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "institute_type",
        "total_members",
        "total_projects",
        "total_publications",
        "total_graduates",
        "total_job_placement",
        "total_gpa",
    ]
    search_fields = ["id", "name"]


@admin.register(EducationInstitute)
class EducationInstituteModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    search_fields = ["id", "user__email"]


@admin.register(RelatedInformation)
class RelatedInformationModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    search_fields = ["id", "user__email"]


@admin.register(UserSkill)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ["id", "skill", "user"]
    search_fields = ["id", "name", "user__email"]
