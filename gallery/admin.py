from django.contrib import admin
from .models import Category, ImageGallery, VideoGallery
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['name', 'slug', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active', 'order']
    ordering = ['order', 'name']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


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


@admin.register(VideoGallery)
class VideoGalleryAdmin(TranslationAdmin):
    list_display = ['id', 'image_preview', 'video_preview', 'title',
                    'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at', 'title']
    list_editable = ['is_active', 'order']
    ordering = ['order', '-created_at']
    fields = ['title', 'video', 'image', 'is_active', 'order']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;">'
        return "No Image"

    def video_preview(self, obj):
        if obj.video:
            return f'<video width="80" height="50" controls><source src="{obj.video.url}" type="video/mp4"></video>'
        return "No Video"

    image_preview.short_description = 'Thumbnail'
    image_preview.allow_tags = True
    video_preview.short_description = 'Video Preview'
    video_preview.allow_tags = True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
