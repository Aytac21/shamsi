from modeltranslation.translator import register, TranslationOptions
from .models import HomeHeader

from django.utils import translation
translation.activate('en')


@register(HomeHeader)
class HomeHeaderTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'category')
