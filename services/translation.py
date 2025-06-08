from modeltranslation.translator import register, TranslationOptions
from .models import Service

from django.utils import translation
translation.activate('en')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
