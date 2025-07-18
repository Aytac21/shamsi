from django.contrib import admin
from .models import Category, ImageWorkshop
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


@admin.register(ImageWorkshop)
class ImageWorkshopAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'image_preview',
                    'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    list_editable = ['is_active',  'order']
    ordering = ['category', 'order', '-created_at']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover;">'
        return "No Image"

    image_preview.short_description = 'Preview'
    image_preview.allow_tags = True
