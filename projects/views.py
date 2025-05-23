from .models import Project
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def project_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = project.images.all()
    context = {
        'project': project,
        'project_images': project_images
    }
    return render(request, 'project-page.html', context)
