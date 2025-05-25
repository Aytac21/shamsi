from django.shortcuts import render
from .models import About, AboutContact, AboutContent, AboutContentSubSection
# Create your views here.


def about_view(request):
    about = About.objects.last()
    aboutcontacts = AboutContact.objects.all()
    aboutcontents = AboutContent.objects.prefetch_related('subsections').all()

    context = {
        'about': about,
        'aboutcontacts': aboutcontacts,
        'aboutcontents': aboutcontents,
    }
    return render(request, 'about.html', context)


