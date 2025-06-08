from modeltranslation.translator import register, TranslationOptions
from .models import Publication

from django.utils import translation
translation.activate('en')


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
