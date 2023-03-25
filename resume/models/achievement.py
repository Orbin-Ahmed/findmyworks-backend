from django.db import models
from core.models import BaseModel


class Achievement(BaseModel):
    user = models.ForeignKey('user.User', related_name="user_achievement", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    links = models.JSONField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    currently_working = models.BooleanField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
