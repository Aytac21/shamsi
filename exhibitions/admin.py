from django.contrib import admin
from .models import Exhibition, ExhibitionImages
from modeltranslation.admin import TranslationAdmin


class ExhibitionImagesInline(admin.TabularInline):
    model = ExhibitionImages
    extra = 3


@admin.register(Exhibition)
class ExhibitionAdmin(TranslationAdmin):
    list_display = ['title', 'description']
    list_filter = ['title']
    search_fields = ['title', 'description']
    inlines = [ExhibitionImagesInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ExhibitionImages)
class ExhibitionImagesAdmin(admin.ModelAdmin):
    list_display = ['exhibition', 'image']
    list_filter = ['exhibition']
