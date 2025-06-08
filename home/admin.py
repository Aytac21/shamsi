from django.contrib import admin
from .models import HomeHeader
from modeltranslation.admin import TranslationAdmin


@admin.register(HomeHeader)
class HomeHeaderAdmin(TranslationAdmin):
    list_display = ('title', 'description', 'url', 'category')
    list_filter = ('title',)
    search_fields = ('title', 'description')
    ordering = ('title',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
