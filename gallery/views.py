from .models import VideoGallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
import json
from .models import ImageGallery, Category, VideoGallery


def gallery_view(request):
    categories = Category.objects.filter(
        is_active=True).order_by('order', 'name')

    category_slug = request.GET.get('category', 'all')

    if category_slug == 'all':
        images = ImageGallery.objects.filter(
            is_active=True).order_by('order', '-created_at')
        active_category = 'all'
    else:
        try:
            category = Category.objects.get(slug=category_slug, is_active=True)
            images = ImageGallery.objects.filter(
                category=category,
                is_active=True
            ).order_by('order', '-created_at')
            active_category = category_slug
        except Category.DoesNotExist:
            images = ImageGallery.objects.filter(
                is_active=True).order_by('order', '-created_at')
            active_category = 'all'

    paginator = Paginator(images, 9)
    page_obj = paginator.get_page(1)

    images_data = []
    for image in page_obj.object_list:
        images_data.append({
            'id': image.id,
            'image_url': image.image.url if image.image else '',
            'category': image.category.name,
        })

    context = {
        'images': page_obj.object_list,
        'categories': categories,
        'active_category': active_category,
        'images_json': json.dumps(images_data),
        'has_more': page_obj.has_next(),
        'total_count': paginator.count,
        'current_page': 1,
        'total_pages': paginator.num_pages
    }
    return render(request, 'gallery.html', context)


def load_more_images(request):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    try:
        page = int(request.GET.get('page', 2))
        category_slug = request.GET.get('category', 'all')

        if page < 1:
            return JsonResponse({'error': 'Invalid page number'}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid page number'}, status=400)

    try:
        if category_slug == 'all':
            images = ImageGallery.objects.filter(
                is_active=True).order_by('order', '-created_at')
        else:
            try:
                category = Category.objects.get(
                    slug=category_slug, is_active=True)
                images = ImageGallery.objects.filter(
                    category=category,
                    is_active=True
                ).order_by('order', '-created_at')
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Category not found'}, status=404)

        paginator = Paginator(images, 9)

        if page > paginator.num_pages:
            return JsonResponse({'error': 'No more images'}, status=404)

        page_obj = paginator.page(page)

        images_data = []
        for image in page_obj.object_list:
            if image.image:
                images_data.append({
                    'id': image.id,
                    'image_url': image.image.url,
                    'category': image.category.name,
                })

        return JsonResponse({
            'images': images_data,
            'has_next': page_obj.has_next(),
            'next_page': page + 1 if page_obj.has_next() else None,
            'current_page': page,
            'total_pages': paginator.num_pages,
            'total_images': paginator.count
        })

    except (EmptyPage, PageNotAnInteger):
        return JsonResponse({'error': 'Invalid page'}, status=400)
    except Exception as e:
        print(f"Gallery error: {str(e)}")
        return JsonResponse({'error': 'Server error occurred'}, status=500)


def gallery_video_view(request):
    videos = VideoGallery.objects.filter(
        is_active=True).order_by('order', '-created_at')
    paginator = Paginator(videos, 6) 
    page_obj = paginator.get_page(1)

    videos_data = []
    for video in page_obj.object_list:
        videos_data.append({
            'id': video.id,
            'image_url': video.image.url if video.image else '',
            'video': video.video,
            'title': video.title
        })

    context = {
        'videos': page_obj.object_list,
        'videos_json': json.dumps(videos_data),
        'has_more': page_obj.has_next(),
        'total_count': paginator.count,
        'current_page': 1,
        'total_pages': paginator.num_pages
    }
    return render(request, 'video.html', context)


def load_more_videos(request):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    try:
        page = int(request.GET.get('page', 2))

        if page < 1:
            return JsonResponse({'error': 'Invalid page number'}, status=400)
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid page number'}, status=400)

    try:
        videos = VideoGallery.objects.filter(
            is_active=True).order_by('order', '-created_at')

        paginator = Paginator(videos, 6)

        if page > paginator.num_pages:
            return JsonResponse({'error': 'No more videos'}, status=404)

        page_obj = paginator.page(page)

        videos_data = []
        for video in page_obj.object_list:
            videos_data.append({
                'id': video.id,
                'image_url': video.image.url if video.image else '',
                'video': video.video,
                'title': video.title
            })

        return JsonResponse({
            'videos': videos_data,
            'has_next': page_obj.has_next(),
            'next_page': page + 1 if page_obj.has_next() else None,
            'current_page': page,
            'total_pages': paginator.num_pages,
            'total_videos': paginator.count
        })

    except (EmptyPage, PageNotAnInteger):
        return JsonResponse({'error': 'Invalid page'}, status=400)
    except Exception as e:
        print(f"Video Gallery error: {str(e)}")
        return JsonResponse({'error': 'Server error occurred'}, status=500)
