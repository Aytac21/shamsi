# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import ImageGallery


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['is_active', 'order']
    readonly_fields = ['image_preview', 'created_at']
    ordering = ['order', '-created_at']

    fields = ('image', 'image_preview', 'is_active',
              'order', 'created_at', 'in_home')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px; object-fit: cover; border-radius: 4px;" />',
                obj.image.url
            )
