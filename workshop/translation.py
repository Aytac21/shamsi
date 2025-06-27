from modeltranslation.translator import register, TranslationOptions
from .models import Category

from django.utils import translation
translation.activate('en')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

