from django.shortcuts import render, get_object_or_404
from .models import Exhibition


def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    exhibition_images = exhibition.images.all()
    context = {
        'exhibition': exhibition,
        'exhibition_images': exhibition_images
    }
    return render(request, 'exhibition-page.html', context)
