from django.db import models
from core.models import BaseModel


class RelatedInformation(BaseModel):
    user = models.OneToOneField('user.User', related_name="user_related_information", on_delete=models.CASCADE)
    image = models.URLField(null=True, blank=True)
    other_skills = models.JSONField(null=True, blank=True)
    social_links = models.JSONField(null=True, blank=True)
    publications = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.id)


class RelatedInformationImage(BaseModel):
    related_information = models.ForeignKey('RelatedInformation', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return str(self.id)
