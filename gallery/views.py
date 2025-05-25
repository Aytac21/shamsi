from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
import json
from .models import ImageGallery


def gallery_view(request):
    images = ImageGallery.objects.filter(is_active=True).order_by(
        '-created_at')

    initial_images = images[:11]
    total_count = images.count()
    has_more = total_count > 11

    images_data = []
    for image in initial_images:
        images_data.append({
            'id': image.id,
            'image_url': image.image.url,
        })

    context = {
        'images': initial_images,
        'images_json': json.dumps(images_data),
        'has_more': has_more,
        'total_count': total_count
    }

    return render(request, 'gallery.html', context)


def load_more_images(request):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    try:
        page = int(request.GET.get('page', 2))
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid page number'}, status=400)

    images = ImageGallery.objects.filter(
        is_active=True).order_by('-created_at')

    paginator = Paginator(images, 1)

    try:
        page_obj = paginator.get_page(page)
    except Exception as e:
        return JsonResponse({'error': 'Invalid page'}, status=400)

    images_data = []
    for image in page_obj.object_list:
        images_data.append({
            'id': image.id,
            'image_url': image.image.url,
        })

    return JsonResponse({
        'images': images_data,
        'has_next': page_obj.has_next(),
        'next_page': page + 1 if page_obj.has_next() else None,
        'current_page': page,
        'total_pages': paginator.num_pages,
        'total_images': paginator.count
    })
