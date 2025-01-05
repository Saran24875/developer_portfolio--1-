from django.contrib import admin
from .models import Developer, Skill, Project

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "developer")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "link")
