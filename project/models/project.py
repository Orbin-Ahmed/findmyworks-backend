from django.db import models
from core.models import BaseModel


class Project(BaseModel):
    user = models.ForeignKey('user.User', related_name="user_project", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=300, null=True, blank=True)
    project_link = models.URLField(null=True, blank=True)
    participants = models.ManyToManyField('user.User')
    project_description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    sponsors_due_date = models.DateField(null=True, blank=True)
    sponsor_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class ProjectImage(BaseModel):
    project = models.ForeignKey('Project', related_name="project_image", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class ProjectActivity(BaseModel):
    project = models.ForeignKey('Project', related_name="project_achievement", on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', related_name="user_project_activity", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return str(self.id)
