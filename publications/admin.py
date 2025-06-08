from django.contrib import admin
from .models import Publication, PublicationImages
from modeltranslation.admin import TranslationAdmin


class PublicationImagesInline(admin.TabularInline):
    model = PublicationImages
    extra = 3


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    inlines = [PublicationImagesInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(PublicationImages)
class PublicationImagesAdmin(admin.ModelAdmin):
    list_display = ['publication', 'image']
    list_filter = ['publication']
