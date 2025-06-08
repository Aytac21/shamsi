from modeltranslation.translator import register, TranslationOptions
from .models import News

from django.utils import translation
translation.activate('en')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
