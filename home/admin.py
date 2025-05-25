from django.contrib import admin
from .models import HomeHeader


@admin.register(HomeHeader)
class HomeHeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'url', 'category')
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)
