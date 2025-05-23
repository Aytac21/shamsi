from django.contrib import admin
from .models import Project, ProjectImages


class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    inlines = [ProjectImagesInline]


@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']
    list_filter = ['project']
