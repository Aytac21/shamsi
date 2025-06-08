from .models import Publication
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string


def home_view(request):
    return render(request, 'index.html')


def publication_list(request):
    publications = Publication.objects.all()

    items_per_page = 6 
    paginator = Paginator(publications, items_per_page)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    has_more = page_obj.has_next()

    context = {
        'publications': page_obj,
        'has_more': has_more,
        'total_count': paginator.count,
        'active_category': request.GET.get('category', ''),
    }

    return render(request, 'publication.html', context)


def load_more_publications(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        page_number = request.GET.get('page', 1)
        category = request.GET.get('category', '')

        publications = Publication.objects.all()
        if category:
            publications = publications.filter(category=category)

        items_per_page = 6
        paginator = Paginator(publications, items_per_page)
        page_obj = paginator.get_page(page_number)

        publications_html = render_to_string('partials/publication_items.html', {
            'publications': page_obj,
        })

        return JsonResponse({
            'html': publications_html,
            'has_more': page_obj.has_next(),
            'next_page': page_obj.next_page_number() if page_obj.has_next() else None,
            'total_count': paginator.count,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    publication_images = publication.images.all()
    context = {
        'publication': publication,
        'publication_images': publication_images
    }
    return render(request, 'publication-page.html', context)
