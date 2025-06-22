from modeltranslation.translator import register, TranslationOptions
from .models import Exhibition

from django.utils import translation
translation.activate('en')


@register(Exhibition)
class ExhibitionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
