from django.shortcuts import render
from .models import Service
# Create your views here.


def services_list(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})
