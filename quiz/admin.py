from django.contrib import admin

from quiz.models import SkillQuizQuestion, SkillQuizResult, Skills


@admin.register(SkillQuizQuestion)
class SkillQuizModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "skill"]
    search_fields = ["id"]


@admin.register(SkillQuizResult)
class SkillQuizResultModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "skill", "result_percent"]
    search_fields = ["id", "user__email"]


@admin.register(Skills)
class SkillQuizResultModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
