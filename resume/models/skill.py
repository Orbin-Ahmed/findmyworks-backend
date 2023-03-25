from django.db import models
from core.models import BaseModel


class UserSkill(BaseModel):
    user = models.ForeignKey('user.User', related_name="user_skill", on_delete=models.CASCADE)
    skill = models.ForeignKey('quiz.Skills', on_delete=models.CASCADE)
    portfolio_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.skill.name)
