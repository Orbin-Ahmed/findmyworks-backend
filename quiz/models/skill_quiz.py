from django.db import models
from core.models import BaseModel


class Skills(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class SkillQuizQuestion(BaseModel):
    skill = models.ForeignKey("quiz.Skills", on_delete=models.CASCADE)
    title = models.CharField(max_length=550)
    a = models.CharField(max_length=350)
    b = models.CharField(max_length=350)
    c = models.CharField(max_length=350, null=True, blank=True)
    d = models.CharField(max_length=350, null=True, blank=True)
    correct_ans = models.CharField(max_length=400)

    def __str__(self):
        return str(self.id)


class SkillQuizResult(BaseModel):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    skill = models.ForeignKey("quiz.Skills", on_delete=models.CASCADE)
    result_percent = models.FloatField()
    status = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.id)
