from django.shortcuts import render
from .models import HomeHeader
from gallery.models import ImageGallery


def home_view(request):
    headers = HomeHeader.objects.all()
    header = HomeHeader.objects.last()

    images = ImageGallery.objects.filter(in_home=True)[:8]

    context = {
        'header': header,
        'headers': headers,
        'images': images
    }
    return render(request, 'index.html', context)