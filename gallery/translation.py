from modeltranslation.translator import register, TranslationOptions
from .models import Category, VideoGallery

from django.utils import translation
translation.activate('en')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(VideoGallery)
class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ('title', )
