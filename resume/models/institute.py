from django.contrib.postgres.fields import ArrayField
from django.db import models
from core.models import BaseModel


class InstituteType(models.TextChoices):
    SCHOOL = "school", "School"
    COLLEGE = "college", "College"
    UNIVERSITY = "university", "University"


class Institute(BaseModel):
    name = models.CharField(max_length=350)
    institute_type = models.CharField(
        "Institute Type",
        max_length=30,
        choices=InstituteType.choices,
    )
    total_members = models.IntegerField(default=0)
    total_projects = models.IntegerField(default=0)
    total_publications = models.IntegerField(default=0)
    total_graduates = models.IntegerField(default=0)
    total_job_placement = models.IntegerField(default=0)
    total_gpa = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class EducationInstitute(BaseModel):
    user = models.ForeignKey('user.User', related_name="user_education_institute", on_delete=models.CASCADE)
    education_type = models.CharField(max_length=150, null=True, blank=True)
    institute = models.ForeignKey('resume.Institute', related_name='education_institute', on_delete=models.CASCADE)
    concentration = models.CharField(max_length=300, null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    currently_studying = models.BooleanField(null=True, blank=True)
    education_board = models.CharField(max_length=150, null=True, blank=True)
    result = models.FloatField(max_length=20, default=0)
    awards = models.JSONField(null=True, blank=True)
    extra_activities = models.JSONField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ProfessionalInstitute(BaseModel):
    user = models.ForeignKey('user.User', related_name="user_professional_institute", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(null=True, blank=True)
    responsibility = ArrayField(
        models.CharField(max_length=500), verbose_name="responsibility", size=50, null=True, blank=True
    )

    def __str__(self):
        return str(self.name)
