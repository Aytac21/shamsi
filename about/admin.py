from django.contrib import admin
from .models import About, AboutContact, AboutContent, AboutContentSubSection


class AboutContactInline(admin.TabularInline):
    model = AboutContact
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutContactInline]
    list_display = ('title', 'description')
    search_fields = ('title', 'description')


class AboutContentSubSectionInline(admin.TabularInline):
    model = AboutContentSubSection
    extra = 1


@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    inlines = [AboutContentSubSectionInline]
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
