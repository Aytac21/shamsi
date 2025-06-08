from modeltranslation.translator import register, TranslationOptions
from .models import (
    About, AboutContact, AboutContent, AboutContentSubSection
)

from django.utils import translation
translation.activate('en')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutContact)
class AboutContactTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(AboutContent)
class AboutContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(AboutContentSubSection)
class AboutContentSubSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
