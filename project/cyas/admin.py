from django.contrib import admin
from .models import Project, Survey


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ["name", "project1", "project2"]



