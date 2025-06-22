from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from .models import Exhibition


def exhibition_list(request):
    exhibitions = Exhibition.objects.all()

    items_per_page = 6
    paginator = Paginator(exhibitions, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'exhibitions': page_obj,
        'has_more': page_obj.has_next(),
        'total_count': paginator.count,
        'active_category': request.GET.get('category', ''),
        'current_page': page_obj.number,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
    }

    return render(request, 'exhibitions.html', context)


def load_more_exhibitions(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        page_number = int(request.GET.get('page', 1))
        category = request.GET.get('category', '')

        exhibitions = Exhibition.objects.all()
        if category:
            exhibitions = exhibitions.filter(category=category)

        items_per_page = 6
        paginator = Paginator(exhibitions, items_per_page)

        if page_number > paginator.num_pages:
            return JsonResponse({
                'html': '',
                'has_more': False,
                'next_page': None,
                'total_count': paginator.count,
                'error': 'Page not found'
            })

        page_obj = paginator.get_page(page_number)

        start_index = (page_number - 1) * items_per_page + 1

        context = {
            'exhibitions': page_obj,
            'start_index': start_index,
        }

        exhibitions_html = render_to_string(
            'partials/exhibition_items.html', context, request=request)

        return JsonResponse({
            'html': exhibitions_html,
            'has_more': page_obj.has_next(),
            'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
            'total_count': paginator.count,
            'current_page': page_number,
            'total_pages': paginator.num_pages,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    exhibition_images = exhibition.images.all()
    context = {
        'exhibition': exhibition,
        'exhibition_images': exhibition_images
    }
    return render(request, 'exhibition-page.html', context)
