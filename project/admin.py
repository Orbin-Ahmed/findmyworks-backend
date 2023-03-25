from django.contrib import admin

from project.models import ProjectImage, Project


@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "user"]
    search_fields = ["id", "title", "user__email"]


@admin.register(ProjectImage)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["id", "project"]
    search_fields = ["id", "project__id"]
