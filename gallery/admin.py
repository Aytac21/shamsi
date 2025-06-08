from django.contrib import admin
from .models import Category, ImageGallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'image_preview',
                    'is_active', 'in_home', 'order', 'created_at']
    list_filter = ['category', 'is_active', 'in_home', 'created_at']
    list_editable = ['is_active', 'in_home', 'order']
    ordering = ['category', 'order', '-created_at']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;">'
        return "No Image"

    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True
